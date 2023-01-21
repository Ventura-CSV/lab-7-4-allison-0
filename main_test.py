import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    # datastr = '90 10 50 40 30'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    l1 = lines[0].strip('[').rstrip(']')
    l1 = list(map(int, l1.split(',')))
    print(l1)

    l2 = lines[1].strip('[').rstrip(']')
    l2 = list(map(int, l2.split(',')))
    print(l2)

    regex_string = ''
    for i in range(len(l1)):
        regex_string += r'[\w,\W]*' + str(l1[i]+l2[i])
    regex_string += r'[\w,\W]*'

    # regex_string = r'[\w,\W]*90'
    # regex_string += r'[\w,\W]*50'
    # regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[2])
    assert res != None
    print(res.group())
