from ctypes import *

def printToken():
    token = windll.Advapi32.GetTokenInformation
    windll.Kernel32.SetLastError()
    dupe = windll.Advapi32.DuplicateTokenEx(token, "TOKEN_ALL_ACCESS", "SecurityImpersonation", "TokenPrimary")
    error = windll.Kernel32.GetLastError()
    print(error)
    print(token)
    print(dupe)


if __name__ == "__main__":
    printToken()