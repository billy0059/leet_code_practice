class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> row_check;
        unordered_set<char> col_check;
        unordered_map<string, unordered_set<char>> grid_check;
        for (int i=0; i<9; i++){
            for (int j=0; j<9; j++){
                if (board[i][j] != '.'){
                    if (row_check.find(board[i][j]) != row_check.end()){ // row check
                        return false;
                    }
                    else{
                        row_check.insert(board[i][j]);
                    }

                    string grid_id(to_string(i/3)+to_string(j/3));
                    if (grid_check[grid_id].find(board[i][j]) != grid_check[grid_id].end()){ // grid check
                        return false;
                    }
                    else{
                        grid_check[grid_id].insert(board[i][j]);
                    }

                }
                if (board[j][i] != '.'){ // col check
                    if (col_check.find(board[j][i]) != col_check.end()){
                        return false;
                    }
                    col_check.insert(board[j][i]);
                }
            }
            row_check.clear();
            col_check.clear();
        }
        return true;
    }
};