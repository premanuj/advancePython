class ClassicalSingleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ClassicalSingleton, cls).__new__(cls)
        return cls.instance


class LazySingleTon:
    __instance = None

    def __init__(self, *args, **kwargs):
        if not LazySingleTon.__instance:
            print("__init__ is called i.e. class initialized but object not created.")
        else:
            print("Instance already created. ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleTon()
        return cls.__instance


if __name__ == "__main__":
    print("========================== Classical Singleton in python ============================")
    s = ClassicalSingleton()
    s.name = "test"
    print("SimpleSingleton Object created (s)", s, s.name)

    s1 = ClassicalSingleton()
    print("SimpleSingleton Object created (s1)", s1, s1.name)

    print("======================================================================================")

    print(
        "========================== Lazy instantiation in Singleton in python ============================"
    )

    s = LazySingleTon()
    print("Object created", LazySingleTon.getInstance())
    s1 = LazySingleTon()
