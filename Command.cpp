#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main() {
    string command;

    while (true) {
        cout << "Command: ";
        getline(cin, command);

        if (command == "exit") {
            cout << "Exiting command prompt." << endl;
            break;
        }

        int result = system(command.c_str());

        if (result != 0) {
            cout << "Command execution failed." << endl;
        }
    }

    return 0;
}
