
class Singleton {

public:

    static Singleton* Instance()
    {
        if(pInstance_)
            return pInstance_;
        return new Singleton;
    }

    int ReturnInt()
    {
        return intValue;
    }

private:

    Singleton() { intValue = 1; }
    Singleton(const Singleton&) {}
    static Singleton* pInstance_;
    int intValue;

};
