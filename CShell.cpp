#include <iostream>
#include <string>
#include <windows.h>

using namespace std;

void executeCommand(const string& command) {
    STARTUPINFO si = {};
    si.cb = sizeof(si);
    PROCESS_INFORMATION pi = {};

    if (!CreateProcess(nullptr, const_cast<LPSTR>(command.c_str()), nullptr, nullptr, FALSE, 0, nullptr, nullptr, &si, &pi)) {
        cerr << "Failed to execute command." << endl;
    }

    WaitForSingleObject(pi.hProcess, INFINITE);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
}

int main() {
    string input;

    while (true) {
        cout << "Shell> ";
        getline(cin, input);

        if (input == "exit") {
            cout << "Exiting shell." << endl;
            break;
        } else {
            executeCommand(input);
        }
    }

    return 0;
}
