#!/usr/bin/env python3

import random
import time

# AWSNetworkingQuiz class - Main class that handles the quiz functionality
class AWSNetworkingQuiz:
    def __init__(self):
        # Initialize score counter to track correct answers
        self.score = 0
        
        # Define quiz questions as a list of dictionaries
        # Each question has:
        # - The question text
        # - Multiple choice options (A, B, C, D)
        # - The correct answer letter
        # - An explanation of the correct answer for learning purposes
        self.questions = [
            {
                "question": "Which AWS service is used to create isolated networks within the AWS cloud?",
                "options": [
                    "A. AWS Direct Connect",
                    "B. Amazon VPC",
                    "C. AWS Transit Gateway",
                    "D. Amazon CloudFront"
                ],
                "correct_answer": "B",
                "explanation": "Amazon VPC (Virtual Private Cloud) allows you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define."
            },
            {
                "question": "Which AWS service helps you establish a dedicated network connection between your premises and AWS?",
                "options": [
                    "A. AWS Direct Connect",
                    "B. AWS VPN",
                    "C. AWS Transit Gateway",
                    "D. Amazon Route 53"
                ],
                "correct_answer": "A",
                "explanation": "AWS Direct Connect is a cloud service that establishes a dedicated network connection from your premises to AWS, providing more consistent network performance than internet-based connections."
            },
            {
                "question": "What is the primary purpose of a Network Access Control List (NACL) in AWS?",
                "options": [
                    "A. To control traffic between subnets in a VPC",
                    "B. To manage access to AWS resources",
                    "C. To encrypt data in transit",
                    "D. To connect multiple VPCs together"
                ],
                "correct_answer": "A",
                "explanation": "Network Access Control Lists (NACLs) act as a firewall for controlling traffic in and out of subnets within your VPC. They operate at the subnet level."
            },
            {
                "question": "Which AWS service allows you to connect multiple VPCs and on-premises networks through a central hub?",
                "options": [
                    "A. AWS PrivateLink",
                    "B. AWS Transit Gateway",
                    "C. AWS Global Accelerator",
                    "D. Amazon CloudFront"
                ],
                "correct_answer": "B",
                "explanation": "AWS Transit Gateway acts as a hub that controls how traffic is routed among all connected networks, which can include VPCs and on-premises networks."
            },
            {
                "question": "What is the difference between Security Groups and NACLs in AWS?",
                "options": [
                    "A. Security Groups operate at the instance level, NACLs at the subnet level",
                    "B. Security Groups operate at the VPC level, NACLs at the instance level",
                    "C. Security Groups are stateless, NACLs are stateful",
                    "D. Security Groups filter only inbound traffic, NACLs filter both inbound and outbound"
                ],
                "correct_answer": "A",
                "explanation": "Security Groups operate at the instance level and are stateful, while NACLs operate at the subnet level and are stateless."
            }
        ]

    # Method to display welcome message and instructions
    def display_welcome(self):
        # Print decorative header with equal signs
        print("\n" + "=" * 50)
        print("WELCOME TO THE AWS NETWORKING QUIZ GAME!")
        print("=" * 50)
        
        # Display instructions for the user
        print("\nTest your knowledge of AWS networking concepts with these 5 questions.")
        print("Choose the correct option (A, B, C, or D) for each question.")
        print("\nLet's get started!\n")
        
        # Brief pause for user to read instructions
        time.sleep(1)

    # Main method to execute the quiz
    def run_quiz(self):
        # Show welcome message
        self.display_welcome()
        
        # Shuffle questions to provide variety each time the quiz is run
        random.shuffle(self.questions)
        
        # Loop through the first 5 questions (or all if less than 5)
        for i, q in enumerate(self.questions[:5]):
            # Display question number and text
            print(f"\nQuestion {i+1}: {q['question']}")
            
            # Display all answer options
            for option in q['options']:
                print(option)
            
            # Input validation loop - ensure user enters a valid option
            while True:
                user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
                if user_answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input! Please enter A, B, C, or D.")
            
            # Check if the answer is correct and provide feedback
            if user_answer == q['correct_answer']:
                print("\n✅ Correct!")
                self.score += 1  # Increment score for correct answers
            else:
                print(f"\n❌ Incorrect! The correct answer is {q['correct_answer']}.")
            
            # Display explanation for educational purposes
            print(f"Explanation: {q['explanation']}")
            
            # Visual separator between questions
            print("\n" + "-" * 50)
            
            # Brief pause between questions
            time.sleep(1)
        
        # After all questions are answered, show final results
        self.display_results()

    # Method to display final quiz results and feedback
    def display_results(self):
        # Print decorative header
        print("\n" + "=" * 50)
        
        # Display final score
        print(f"QUIZ COMPLETED! Your score: {self.score}/5")
        
        # Provide personalized feedback based on score
        if self.score == 5:
            print("Perfect score! You're an AWS networking expert!")
        elif self.score >= 3:
            print("Good job! You have solid AWS networking knowledge.")
        else:
            print("Keep learning! AWS networking concepts take time to master.")
        
        # Print decorative footer
        print("=" * 50 + "\n")

# Entry point of the program
# This conditional ensures the quiz only runs when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    # Create an instance of the quiz
    quiz = AWSNetworkingQuiz()
    
    # Start the quiz
    quiz.run_quiz()