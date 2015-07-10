from pdserver.model import names


def testNameGeneration():
    assert 'pd.damouse' == names.idForUser('damouse')
    assert 'pd.damouse.chutes.netflix-2' == names.idForChute('damouse', 'netflix', 2)
    assert 'pd.damouse.routers.aardvark' == names.idForRouter('damouse', 'aardvark')
    assert 'pd.damouse.routers.aardvark.instances.netflix-2' == names.idForInstance('damouse', 'aardvark', 'netflix', 2)
    assert 'pd.damouse.groups.castle' == names.idForGroup('damouse', 'castle')


# def testHumanReadable():
#     assert names.formatHuman('pd.damouse') == 'pd.damouse'
#     assert names.formatHuman('pd.damouse.chutes.netflix-2') == 'pd.damouse.netflix'
#     assert names.formatHuman('pd.damouse.routers.aardvark') == 'pd.damouse.aardvark'
#     assert names.formatHuman('pd.damouse.routers.aardvark.instances.netflix-2') == 'pd.damouse.aardvark.netflix'
