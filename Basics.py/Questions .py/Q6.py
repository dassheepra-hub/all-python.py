def is_dot_com_or_dot_in (domain):
    return domain.endswith (".com") or domain.endswith (".in")

exam1 = is_dot_com_or_dot_in ("eample.com")
print(exam1)
