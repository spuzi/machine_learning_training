import funciones_generales


def test_add():
    assert funciones_generales.add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

    try:
        funciones_generales.add([1, 2, 3], [4, 5])
    except Exception as e:
        assert str(e) == "vectors must be the same length"


test_add()
