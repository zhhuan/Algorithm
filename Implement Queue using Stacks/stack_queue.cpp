#include <iostream>
using namespace std;

struct StackN{
	int elem;
	StackN* next;
};

class CStack{
public:
	StackN* head;
	int size;
	CStack(){
		head = new StackN;
		head->next = NULL;
		size = 0;
	}
	
	CStack(CStack& oldStack){
		size = oldStack.size;
		StackN* pOldStack;
		StackN* pNewStack;
		StackN* pTail;
		
		pOldStack = new StackN;
		pOldStack = oldStack.head->next;
		pTail = head;
		while(pOldStack!=NULL){
			pNewStack = new StackN;
			pNewStack->next = NULL;
			pNewStack->elem = pOldStack->elem;
			pOldStack = pOldStack->next;
			pTail->next = pNewStack;
			pTail = pNewStack;
		}
	}
	//push element to the head of stack
	void push(int x){
		StackN* temp_N;
		temp_N = new StackN;
		temp_N->elem = x;
		temp_N->next = head->next;
		head->next = temp_N;
		size++;
	}
	
	//remove the element in the head
	void pop(){
		StackN* pop_stack ;
		if(head->next == NULL)
			exit(1);
		else{
			pop_stack = head->next;
			head->next = pop_stack->next;
			delete pop_stack;
		}
	}

	//get the top element
	int peek(){
		return head->next->elem;
	}
	
	//return whether the stack is empty
	bool isempty(){
		if(head->next == NULL)
			return true;
		else
			return false;
	}
};

class Queue{
private:
	CStack s1;
	CStack s2;	
public:
	int length;
	Queue(){
		length = 0;
	}
	//Push element x to the back of queue.
	void push(int x){
		int temp;
		while(s2.head->next!=NULL){
			temp = s2.peek();
			s2.pop();
			s1.push(temp);
		}
		s1.push(x);
		length++;
	}
	// Removes the element from in front of queue.
	void pop(){
		int temp;
		while(s1.head->next != NULL){
			temp = s1.peek();
			s1.pop();
			s2.push(temp);
		}
		s2.pop();
		length--;
	}
	//Get the front element
	int peek(){
		int temp, front;
		while(s1.head->next != NULL){
			temp = s1.peek();
			s1.pop();
			s2.push(temp);
		}
		front = s2.peek(); 	
		return front;
	}
	//return whether the quene is empty.
	bool empty(){
		if(0 == length)
			return true;
		else return false;
	}
};
#endif