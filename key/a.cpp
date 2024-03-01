#include <vector>
#include <iostream>
#include <fstream> // for file output
using namespace std;
#define INF 2147483647

template <class value_type>
void printHTMLTable(vector<vector<value_type>> v, ofstream& outFile) {
    outFile << "<table border=\"1\">" << endl;
    for (int i = 1; i < v.size(); i++) {
        outFile << "<tr>";
        for (int j = 1; j < v[i].size(); j++) {
            outFile << "<td>";
            if (v[i][j] == INF)
                outFile << "X";
            else
                outFile << v[i][j];
            outFile << "</td>";
        }
        outFile << "</tr>" << endl;
    }
    outFile << "</table>" << endl;
}

void optimal_bst(vector<double> p, vector<double> q, vector<vector<double>>& e, vector<vector<int>>& root, ofstream& outFile) {

    int i, j, k, l;
    double temp;
    vector<vector<double>> w(q.size() + 1, vector<double>(q.size()));

    for (i = 1; i <= q.size(); i++) {
        e[i][i - 1] = q[i - 1];
        w[i][i - 1] = q[i - 1];
    }
    for (l = 1; l < q.size(); l++)
        for (i = 1; i < q.size() - l + 1; i++) {
            j = i + l - 1;
            for (k = i; k <= j; k++) {
                w[i][j] = w[i][k - 1] + p[k] + w[k + 1][j];
                temp = e[i][k - 1] + e[k + 1][j] + w[i][j];
                if (temp < e[i][j]) {
                    e[i][j] = temp;
                    root[i][j] = k;
                }
            }
        }
    outFile << "<h3>Cost</h3>" << endl;
    printHTMLTable(e, outFile);
    outFile << "<br><br>" << endl;
    outFile << "<h3>Weight</h3>" << endl;
    printHTMLTable(w, outFile);
    outFile << "<br><br>" << endl;
    outFile << "<h3>Root</h3>" << endl;
    printHTMLTable(root, outFile);
    outFile << "<br><br>" << endl;
}

int main() {

    vector<double> p = { 0,0.04,0.06,0.08,0.02,0.1,0.12,0.14 };
    vector<double> q = { 0.06,0.06,0.06,0.06,0.05,0.05,0.05,0.05 };

    ofstream outFile("output.html");
    if (outFile.is_open()) {
        outFile << "<!DOCTYPE html>" << endl;
        outFile << "<html><head><title>Optimal BST</title></head><body>" << endl;
        vector<vector<double>> e(q.size() + 1, vector<double>(q.size(), INF));
        vector<vector<int>> root(q.size(), vector<int>(q.size(), 0));
        optimal_bst(p, q, e, root, outFile);
        outFile << "</body></html>" << endl;
        outFile.close();
        cout << "Output has been written to output.html" << endl;
    }
    else {
        cout << "Unable to open file." << endl;
    }
    return 0;
}
