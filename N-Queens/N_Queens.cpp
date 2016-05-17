/*
*@author:Zhong Huan
*@date:2016/5/18
*1.N-Queens:print all solutions like:
* .Q..
* ...Q
* Q...
* ..Q.
*2.N-Queens II:Follow up for N-Queens problem.Now, instead outputting board configurations, 
*return the total number of distinct solutions.
*
*/
#include <stdio.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <string>
using namespace std;

class Solution {
public:
  vector<vector<string>> solveNQueens(int n) {//int totalNQueens(int n)
    vector<vector<string>> all_nqueens;
    vector<string> nqueens(n, string(n, '.'));
    vector<int> N_q(n, 0);
    int cur_row = 0;
    while (1) {
      if (cur_row == n ) {
        for (int col = 0; col != n; col++) {
          nqueens[col][N_q[col]] = 'Q';
        }
        all_nqueens.push_back(nqueens);
        for (vector<string>::iterator iter = nqueens.begin();
        iter != nqueens.end(); ++iter) {
          *iter=(n, string(n, '.'));
        }
        cur_row -= 1;
        cur_row = seek_back(N_q, cur_row, n) + 1;
        if(cur_row == 0)
          return all_nqueens;//return all_queens.size();
      }
      else if (cur_row < n ) {
        if (search_col(N_q, cur_row, n))
          cur_row++;
        else {
          cur_row = seek_back(N_q, cur_row, n)+1;
          if (cur_row == 0)
            return all_nqueens;//return all_queens.size();
        }
      }
    }
  }

  


  /*
  *@name:search_col
  *@parameter:current queen row number
  *@ret:next queen's column number
  */
  bool search_col(vector<int> &N_q, int cur_row,int n) {
    for (vector<int>::size_type col = 0; col != n; col++) {
      N_q[cur_row] = col;
      if (queen_judge(N_q, cur_row))
        return true;
    }
    return false;
  }
  /*
  *@name:seek_back
  *@parameter: current queen row number
  *@ret:none
  */
  int seek_back(vector<int> &N_q,int cur_row,int n) {
    while (1) {
      N_q[cur_row] = 0;
      cur_row--;
      if (cur_row == -1)
        return -1 ;
      for (int j = N_q[cur_row] + 1; j < n; j++) {
        N_q[cur_row] = j;
        if (queen_judge(N_q, cur_row))
          return cur_row;
      }
    }
  }
  /*
  *@name:queen_judge
  *@parameter:current queen row number
  *@ret:bool
  */
  bool queen_judge(vector<int> &N_q,int cur_row) {
    for (int j = 0; j < cur_row; j++) {
      if (N_q[j] == N_q[cur_row])
        return false;
      else if (abs(N_q[cur_row] - N_q[j]) == cur_row - j)
        return false;
    }
    return true;
  }
};

void main() {
  Solution s;
  vector<vector<string>> str;
  str = s.solveNQueens(4);
  for (vector<vector<string>>::iterator ite = str.begin(); ite != str.end(); ite++) {
    vector<string> each_s = *ite;
    for (vector<string>::iterator itstr = each_s.begin(); itstr != each_s.end(); itstr++) {
      cout << *itstr << endl;
    }
  }
  
}