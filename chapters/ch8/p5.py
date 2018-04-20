'''
Develop a terminal-based program that allows a bank manager to manip- ulate the accounts in a bank.
This menu-driven program should include all of the relevant options,
such as adding a new account, removing an account, and editing an account.
'''


class account:
    def __init__(self, fname, lname, accountnum, ballance):
        self._fname = fname
        self._lname = lname
        self._accountNum = accountnum
        self._ballance = ballance

    def __str__(self):
        return 'first name ', self._fname, ' last name ', self._lname, ' account number ', self._accountNum, ' ballance ', self._ballance

    def saveString(self):
        return self._fname, ',', self._lname, ',', self._accountNum, ',', self._ballance


accounts = list()


def addAccount(fname='john', lname='do', accountNum=00000, ballance=0, accounts=list()):
    accounts.append(account(fname, lname, accountNum, ballance))
    acSave(accounts)
    print('you are creating an acount belonging to ', fname, ' ', lname, ' with the account number ', accountNum,
          ' and a balance of ', ballance)


def delleatAcount(fname, lname, acountnum, accounts=list()):
    index = findAcount(fname, lname, accountnum)
    accounts.remove(index)

    print("are you sure you want to deleat account", acountnum, 'belonging to ', fname, ' ', lname)
