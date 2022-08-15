# moudle search path

""""
python start search in 
1- home path
2- PYTHONPATH directory
3- standard library
4- site package which is third party extension
all of them would create 
"""


def moduleSearch():
    """to add path to python use append command"""
    import sys
    import os
    module = os.path.join("c:\\", "test")
    sys.path.append(module)

    import t2
    t2.modulFunction()
    from t2 import modulFunction
    modulFunction()

    print(t2.__dict__['modulFunction']())
    # u can use import x1.x2
    # from x1.x2 import y1


moduleSearch()
