#include<bits/stdc++.h>

using namespace std;

const int namesSZ = 300;
string names[] = {"Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David", "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan", "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa", "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany", "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Crystal", "Michelle", "Tiffany", "Jeremy", "Benjamin", "Mark", "Emily", "Aaron", "Charles", "Rebecca", "Jacob", "Stephen", "Patrick", "Sean", "Erin", "Zachary", "Jamie", "Kelly", "Samantha", "Nathan", "Sara", "Dustin", "Paul", "Angela", "Tyler", "Scott", "Katherine", "Andrea", "Gregory", "Erica", "Mary", "Travis", "Lisa", "Kenneth", "Bryan", "Lindsey", "Kristen", "Jose", "Alexander", "Jesse", "Katie", "Lindsay", "Shannon", "Vanessa", "Courtney", "Christine", "Alicia", "Cody", "Allison", "Bradley", "Samuel", "Shawn", "April", "Derek", "Kathryn", "Kristin", "Chad", "Jenna", "Tara", "Maria", "Krystal", "Jared", "Anna", "Edward", "Julie", "Peter", "Holly", "Marcus", "Kristina", "Natalie", "Jordan", "Victoria", "Jacqueline", "Corey", "Keith", "Monica", "Juan", "Donald", "Cassandra", "Meghan", "Joel", "Shane", "Phillip", "Patricia", "Brett", "Ronald", "Catherine", "George", "Antonio", "Cynthia", "Stacy", "Kathleen", "Raymond", "Carlos", "Brandi", "Douglas", "Nathaniel", "Ian", "Craig", "Brandy", "Alex", "Valerie", "Veronica", "Cory", "Whitney", "Gary", "Derrick", "Philip", "Luis", "Diana", "Chelsea", "Leslie", "Caitlin", "Leah", "Natasha", "Erika", "Casey", "Latoya", "Erik", "Dana", "Victor", "Brent", "Dominique", "Frank", "Brittney", "Evan", "Gabriel", "Julia", "Candice", "Karen", "Melanie", "Adrian", "Stacey", "Margaret", "Sheena", "Wesley", "Vincent", "Alexandra", "Katrina", "Bethany", "Nichole", "Larry", "Jeffery", "Curtis", "Carrie", "Todd", "Blake", "Christian", "Randy", "Dennis", "Alison", "Trevor", "Seth", "Kara", "Joanna", "Rachael", "Luke", "Felicia", "Brooke", "Austin", "Candace", "Jasmine", "Jesus", "Alan", "Susan", "Sandra", "Tracy", "Kayla", "Nancy", "Tina", "Krystle", "Russell", "Jeremiah", "Carl", "Miguel", "Tony", "Alexis", "Gina", "Jillian", "Pamela", "Mitchell", "Hannah", "Renee", "Denise", "Molly", "Jerry", "Misty", "Mario", "Johnathan", "Jaclyn", "Brenda", "Terry", "Lacey", "Shaun", "Devin", "Heidi", "Troy", "Lucas", "Desiree", "Jorge", "Andre", "Morgan", "Drew", "Sabrina", "Miranda", "Alyssa", "Alisha", "Teresa", "Johnny", "Meagan", "Allen", "Krista", "Marc", "Tabitha", "Lance", "Ricardo", "Martin", "Chase", "Theresa", "Melinda", "Monique", "Tanya", "Linda", "Kristopher", "Bobby", "Caleb", "Ashlee", "Kelli", "Henry", "Garrett", "Mallory", "Jill", "Jonathon", "Kristy", "Anne", "Francisco", "Danny", "Robin", "Lee", "Tamara", "Manuel", "Meredith", "Colleen", "Lawrence", "Christy", "Ricky", "Randall", "Marissa", "Ross", "Mathew", "Jimmy", "Abigail", "Kendra", "Carolyn", "Billy", "Deanna", "Jenny", "Jon", "Albert", "Taylor", "Lori", "Rebekah", "Cameron", "Ebony", "Wendy", "Angel", "Micheal", "Kristi", "Caroline", "Colin", "Dawn", "Kari", "Clayton", "Arthur", "Roger", "Roberto", "Priscilla", "Darren", "Kelsey", "Clinton", "Walter", "Louis", "Barbara", "Isaac", "Cassie", "Grant", "Cristina", "Tonya", "Rodney", "Bridget", "Joe"};

const int agentClassesSZ = 4;
string agentClasses[] = {"duelists", "controllers", "initiators", "sentinels"};

const int mapsSZ = 6;
string maps[] = {"bind", "haven", "split", "ascent", "icebox", "breeze"};

const int gameModesSZ= 3;
string gameModes[] = {"ranked", "unranked", "spikerush"};

const int regionsSZ = 6;
string regions[] = {"NA", "LATAM", "BR", "EU", "KR", "AP"};

string s(string x){
	return "\"" + x + "\"";
}
string ranBool(){
	int t = rand()%2;
	if(t==0) return "FALSE";
	else return "TRUE";
}

string ranDate(){
	int d = 1 + rand()%25;
	int m = 1 + rand()%12;
	int y = 2000 + rand()%22;
	char buf[1024];
	sprintf(buf, "%04d-%02d-%02d", y, m, d);
	string str(buf);
	return str;
}

string ranTime(){
	int h = 0 + rand()%24;
	int m = 0 + rand()%60;
	int s = 0 + rand()%60;
	char buf[1024];
	sprintf(buf, "%02d:%02d:%02d", h, m, s);
	string str(buf);
	return str;
}

string ranDateTime(){
	return ranDate() + " " + ranTime();
}

string ranMap(){
	int id = rand()%mapsSZ;
	return maps[id];
}

string ranAgentClass(){
	int id = rand()%agentClassesSZ;
	return agentClasses[id];
}

string ranGameMode(){
	int id = rand()%gameModesSZ;
	return gameModes[id];
}

string ranRating(){
	int rr = rand()%2000;
	return to_string(rr);
}

string ranRRDelta(){
	int rr_delta = rand()%20;
	return to_string(rr_delta);
}

string ranTag(){
	char a = 'A' + rand()%26;
	char b = 'A' + rand()%26;
	char c = '0' + rand()%10;
	char d = 'A' + rand()%26;
	string tag = "";
	tag += a; tag += b;	tag += c; tag += d;
	return tag;
}

string ranName(){
	int id = rand()%namesSZ;
	return names[id];
}

string ranInt(int s, int e){
	int t = s + rand()%(e-s+1);
	return to_string(t);
}

string ranRegion(){
	int id = rand()%regionsSZ;
	return regions[id];
}

set<string> usedNames;
void createPlayer(){
	cout<<"INSERT INTO player VALUES (";
	string name = ranName();
	while(usedNames.find(name)!=usedNames.end())
		name = ranName();
	usedNames.insert(name);

	cout << s(name) << ", " << s(ranTag()) << ", " << s(ranDate()) << ", " << s(ranTime()) << ", " << ranRating() << ", " << s(ranRegion());
	cout << ", NULL, NULL);" << endl;
	
}

int main(void){
	srand(time(0));
	for(int i=0; i<20; i++){
		createPlayer();
	}
	createPlayer();
}