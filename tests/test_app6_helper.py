from app6.common.helper import FamilyMember, generate_family, rand_member


class TestClass:

    def test_helper_returns_family_member(self):
        x = rand_member()
        assert isinstance(x, FamilyMember)
        assert isinstance(x.name, str)
        assert len(x.chores) >= 1

    def test_generate_family(self):
        x = generate_family()
        assert isinstance(x, list)
        assert len(x) >= 2
        assert all([isinstance(i, FamilyMember) for i in x])
