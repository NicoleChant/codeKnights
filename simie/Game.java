import java.util.ArrayList;

public class Game{

    public static void main(String[] args){
      ArrayList<Player> participants = new ArrayList<Player>();
      participants.add(new Player("Nicole",100,30,10,0.3));
      participants.add(new Player("Bob",130,23,13,0.2));
      participants.add(new Player("Alice",150,15,12,0.1));

      for(int i = 0 ; i < participants.size() ; ++ i){
        participants.get(i).setTarget(participants.get((i+1)%participants.size()));
      }

      for(Player participant : participants){
        participant.attack();
      }

      for(Player participant : participants){
        if(!participant.isAlive()){
          System.out.println("Player " + participant.name + " has deceased :(");
        }
      }

}
}
