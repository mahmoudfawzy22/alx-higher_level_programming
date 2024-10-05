def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    is_empty = True

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if row:
            is_empty = False
        
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(" m_a should contain only integers or floats")

        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(" m_a should contain only integers or floats")

    is_empty_2 = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if row:
            is_empty_2 = False
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_b must be of the same size ")
        
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(" m_b should contain only integers or floats")
    
    if is_empty or is_empty_2:
        raise TypeError("m_a  or m_b can't be empty")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    res = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")