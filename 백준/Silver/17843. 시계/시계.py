t = int(input())
for i in range(t):
    h, m, s = map(int, input().split())
    
    s_degree = s * 6
    m_degree = m * 6 + s * 0.1
    h_degree = h * 30 + m * 0.5 + s * (1/120)

    min_degree = min(abs(h_degree - m_degree), abs(h_degree - s_degree), abs(m_degree - s_degree), 360 - abs(h_degree - m_degree), 360 - abs(h_degree - s_degree), 360 - abs(m_degree - s_degree))

    print(f'{min_degree:.6f}')