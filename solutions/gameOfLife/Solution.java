class Solution {



    public static void main(String[] args){
      int[][] board =  { {0,1,0} ,{0,0,1},{1,1,1} , {0,0,0} };
      getBoard(board);
      gameOfLife(board);
      System.out.println("New Generation!");
      getBoard(board);
      }

      public static void getBoard(int [][] board){
          for(int i = 0 ; i < board.length ; ++i){
                for(int j = 0 ; j < board[0].length; ++j){
                  System.out.print(board[i][j] + " ");
                }
                System.out.println();
          }
      }

    public static void gameOfLife(int[][] board) {
        byte counter;

        for(int i = 0; i<board.length; ++i){
            for(int j = 0 ; j<board[0].length ; ++j){
                counter = 0;
                for(int n=1;n>-2;--n){
                    for(int m=1;m>-2;--m){
                        try{
                            if(board[i+n][j+m]%2==1 && (n!=0 || m!=0)){
                                    ++counter;
                                }

                        }
                        catch(Exception e){
                            continue;
                        }
                    }
                    if(counter>3){break;}
                }

                if(board[i][j]%2 == 1){
                      board[i][j] = (counter == 2 || counter == 3) ? 1 : 3;
                }
                else {
                  board[i][j] = (counter== 3) ? 2 : 0;
                }

            }
        }

        for(int i = 0 ; i < board.length ; ++i){
            for(int j = 0 ; j < board[0].length ; ++j){
                if( board[i][j] == 3){
                  board[i][j] = 0;
                }
                else if(board[i][j]==2){
                  board[i][j] = 1;
                }
            }
        }
    }
}
