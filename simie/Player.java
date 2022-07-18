import java.util.ArrayList;
import java.util.Random;

public class Player{

    public String name;
    private double health;
    private double maxHealth;
    private double damage;
    private double armor;
    private double criticalChance;
    private Player target = null;
    private Random dmgGenerator = new Random();


    public Player(String name , double health , double damage , double armor , double criticalChance){
      this.name = name;
      this.health = health;
      this.damage = damage;
      this.armor = armor;
      this.criticalChance = criticalChance;
      this.maxHealth = this.health;
    }

    public boolean isAlive(){
      return this.health > 0;
    }

    static double damageReduction(double armor){
      return 1 - armor/(armor + 100);
    }

    public void resurrect(){
      this.health = this.maxHealth;
    }

    public String toString(){
      return this.name;
    }

    public void setTarget(Player target){
      this.target = target;
    }

    public double RND(){
      return this.dmgGenerator.nextDouble()*this.damage*30;
    }

    public void attack(){
      double unmitigatedDamage = this.RND();
      double mitigatedDamage = this.RND()*Player.damageReduction(this.armor);
      this.target.health -= unmitigatedDamage;
      System.out.println("Player " + this.name + " strikes player " + this.target.name + " for " + mitigatedDamage +  " physical damage!");
    }

  }
