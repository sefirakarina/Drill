#include<iostream>
#include<string>
using namespace std ;

class Author
{
	string name ;
	string email ;
	char gender ;
	
	public :
	
	Author(){
	}
	
	Author(string namee,string emaill,char genderr)
	{
		name=namee;
		email=emaill;
		gender=genderr;
	}
	
	string getName()
	{
		return name ;
	}
	
	string getEmail()
	{
		return email ;
	}

	char getGender()
	{
		return gender ;
	}  
	
	string toString()
    {
        string Author = name + "\n" + email + "\n" + gender;
        
        return Author;

    }
	
};

int main()
{
	string namee,emaill;
	char genderr ;
	Author input ;
	

	cout<<"input name\t : " ;
	cin>>namee;
	
	cout<<"input email\t : " ;
	cin>>emaill ;
	
	cout<<"input gender(F/M) : ";
	cin>>genderr ; 
	

	
	Author print(namee,emaill,genderr);
    cout << print.toString();
	
	
	return 0;
}


