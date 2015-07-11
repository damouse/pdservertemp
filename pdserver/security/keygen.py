import OpenSSL
from OpenSSL import crypto
import os
# from OpenSSL import crypto

TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA


def createKeyPair(type, bits):
    """
    Create a public/private key pair.

    Arguments: type - Key type, must be one of TYPE_RSA and TYPE_DSA
               bits - Number of bits to use in the key
    Returns:   The public/private key pair in a PKey object
    """
    pkey = crypto.PKey()
    pkey.generate_key(type, bits)
    return pkey


def createCertRequest(pkey, digest="sha256", **name):
    """
    Create a certificate request.

    Arguments: pkey   - The key to associate with the request
               digest - Digestion method to use for signing, default is sha256
               **name - The name of the subject of the request, possible
                        arguments are:
                          C     - Country name
                          ST    - State or province name
                          L     - Locality name
                          O     - Organization name
                          OU    - Organizational unit name
                          CN    - Common name
                          emailAddress - E-mail address
    Returns:   The certificate request in an X509Req object
    """
    req = crypto.X509Req()
    subj = req.get_subject()

    for key, value in name.items():
        setattr(subj, key, value)

    req.set_pubkey(pkey)
    req.sign(pkey, digest)
    return req


def createCertificate(req, issuerCertKey, serial, validityPeriod, digest="sha256"):
    """
    Generate a certificate given a certificate request.

    Arguments: req        - Certificate reqeust to use
               issuerCert - The certificate of the issuer
               issuerKey  - The private key of the issuer
               serial     - Serial number for the certificate
               notBefore  - Timestamp (relative to now) when the certificate
                            starts being valid
               notAfter   - Timestamp (relative to now) when the certificate
                            stops being valid
               digest     - Digest method to use for signing, default is sha256
    Returns:   The signed certificate in an X509 object
    """
    issuerCert, issuerKey = issuerCertKey
    notBefore, notAfter = validityPeriod
    cert = crypto.X509()
    cert.set_serial_number(serial)
    cert.gmtime_adj_notBefore(notBefore)
    cert.gmtime_adj_notAfter(notAfter)
    cert.set_issuer(issuerCert.get_subject())
    cert.set_subject(req.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(issuerKey, digest)
    return cert


def main():
    cakey = createKeyPair(TYPE_RSA, 2048)
    careq = createCertRequest(cakey, CN='Certificate Authority')
    cacert = createCertificate(careq, (careq, cakey), 0, (0, 60 * 60 * 24 * 365 * 5))  # five years

    print('Creating Certificate Authority private key in "simple/CA.pkey"')
    with open(os.getcwd() + 'CA.pkey', 'w') as capkey:
        capkey.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, cakey).decode('utf-8'))

    print('Creating Certificate Authority certificate in "simple/CA.cert"')
    with open(os.getcwd() + 'CA.cert', 'w') as ca:
        ca.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cacert).decode('utf-8'))

    for (fname, cname) in [('client', 'Simple Client'), ('server', 'Simple Server')]:
        pkey = createKeyPair(TYPE_RSA, 2048)
        req = createCertRequest(pkey, CN=cname)
        cert = createCertificate(req, (cacert, cakey), 1, (0, 60 * 60 * 24 * 365 * 5))  # five years
        print('Creating Certificate %s private key in "simple/%s.pkey"' % (fname, fname))
        with open(os.getcwd() + '%s.pkey' % (fname,), 'w') as leafpkey:
            leafpkey.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey).decode('utf-8'))
        print('Creating Certificate %s certificate in "simple/%s.cert"' % (fname, fname))
        with open(os.getcwd() + '%s.cert' % (fname,), 'w') as leafcert:
            leafcert.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8'))


if __name__ == '__main__':
    main()
