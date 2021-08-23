import unittest

from d_serialize import d_serialize


class ClassNoPublicProperties:
    _float_value = 1.1

    def __init__(self, float_value=None):
        if float_value is not None:
            self._float_value = float_value

    def __str__(self):
        return f"{self._float_value}"


class ClassWithProperties:
    one_value = 1
    two_value = 2.2
    string_value = 'string'
    list_value = [1, 'a', dict(b='b'), 2.2, ClassNoPublicProperties()]

    @classmethod
    def test_value(cls):
        return dict(one_value=1, two_value=2.2, string_value='string', list_value=[1, 'a', {'b': 'b'}, 2.2, "1.1"])


class MyTestCase(unittest.TestCase):
    def test_simple_dict(self):
        d = dict(number_value=1, float_value=1.1, boolean_value=True, str_value='hello')
        serialized = d_serialize(d)
        self.assertEqual(d, serialized)

    def test_simple_list(self):
        d = dict(list_value=[1, 2, 3])
        serialized = d_serialize(d)
        self.assertEqual(d, serialized)

    def test_simple_set(self):
        d = dict(set_value={1, 2, 3})
        serialized = d_serialize(d)
        self.assertEqual(dict(set_value=[1,2,3]), serialized)

    def test_simple_tuple(self):
        d = dict(set_value=(1, 2))
        serialized = d_serialize(d)
        self.assertEqual(dict(set_value=[1,2]), serialized)

    def test_list_with_dict(self):
        d = dict(list_value=[dict(a='a'), 2, 3])
        serialized = d_serialize(d)
        self.assertEqual(d, serialized)

    def test_simple_obj(self):
        class TestObject:
            number_value = 1
            float_value = 1.1
            boolean_true_value = True
            str_value = 'hello'

        expected = dict(number_value=1, float_value=1.1, boolean_true_value=True, str_value='hello')
        serialized = d_serialize(TestObject())
        self.assertEqual(expected, serialized)

    def test_obj_with_methods(self):
        class TestObject:
            number_value = 1
            float_value = 1.1

            def dont_call_me(self):
                """return self.number_value"""

        expected = dict(number_value=1, float_value=1.1)
        serialized = d_serialize(TestObject())
        self.assertEqual(expected, serialized)

    def test_obj_property(self):
        class TestObject:
            number_value = 1
            float_value = 1.1
            boolean_true_value = True
            str_value = 'hello'
            class_float_value = ClassNoPublicProperties(2.2)

            @property
            def prop(self):
                return 'prop'

        expected = dict(number_value=1, float_value=1.1, boolean_true_value=True, str_value='hello', prop='prop',
                        class_float_value='2.2')
        serialized = d_serialize(TestObject())
        self.assertEqual(expected, serialized)

    def test_obj_object_as_property(self):
        class TestObject:
            number_value = 1
            _class_value = ClassWithProperties()

            @property
            def prop(self):
                return self._class_value

        expected = dict(number_value=1, prop=ClassWithProperties.test_value())
        serialized = d_serialize(TestObject())
        self.assertEqual(expected, serialized)

    def test_obj_complex_property(self):
        class TestObject:
            number_value = 1
            _complex_object = ClassWithProperties()

            @property
            def complex_object(self):
                return self._complex_object

        expected = dict(number_value=1, complex_object=ClassWithProperties.test_value())
        serialized = d_serialize(TestObject())
        self.assertEqual(expected, serialized)


if __name__ == '__main__':
    unittest.main()
