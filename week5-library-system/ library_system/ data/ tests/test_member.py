from library_system.member import Member

def test_member_creation():
    member = Member("MEM001", "Asha")
    assert member.name == "Asha"
