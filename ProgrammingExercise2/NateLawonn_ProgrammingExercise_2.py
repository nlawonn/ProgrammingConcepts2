def main():
    while True:
        spam_score = 0
        found_keywords = []
        spam = ['free', 'winner', 'congratulations', 'act now', 'limited time', 'urgent', 'offer expires',
            'click here', 'buy now', 'risk-free', 'guaranteed', 'no cost', 'special promotion', 'prize',
            'lowest price', 'claim your reward', 'instant access', 'exclusive deal', 'work from home',
            'make money', 'earn cash', 'million dollars', 'cheap', 'discount', 'unsubscribe',
            'account suspended', 'verify your account', 'password reset', 'payment required',
            'click to confirm'
            ]
        #Asks the user to enter email text
        email = input('Please enter your email message to check for spam. ')

        #Checks the email against spam list and appends each match to found_keywords
        for item in spam:
            if item in email.lower():
                spam_score += 1
                found_keywords.append(item)
        break
    return spam_score, email, found_keywords

def spam_calc(spam_score, email, found_keywords):

    #Calculates spam score, identifies keywords
    if spam_score == 0:
        print("Your spam score is zero. No keywords were identified.")
    else:
        print(f"Your spam score is {spam_score}. Keywords identified are {", ".join(found_keywords)}.")

        #Prints spam likelihood
        if spam_score < 3:
            print("Likelihood of spam is low.")
        elif spam_score < 6:
            print("Likelihood of spam is medium.")
        else:
            print("Likelihood of spam is high.")
        return spam_score, email, found_keywords

if __name__ == "__main__":
# 1. Run main() and capture what it returns into variables
    score_result, email_result, keywords_result = main()

 # 2. Pass those captured variables into spam_calc
    spam_calc(score_result, email_result, keywords_result)