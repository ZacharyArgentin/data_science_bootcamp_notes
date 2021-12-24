# Machine Learning vs Deep Learning

What is AI?
- The simulation of human logic and reasoning by computers

Knowledge base AI
  - Hard coded "Logic rules" for a computer program to follow.
  - Not very successful attempts at AI because it's impossible to account for every possibility in reality.

Machine learning solves this problem by taking the data and the desired output and the computer comes up with the rules required.
  - e.g. data + desired output --> program   

Knowledge based AI would start with the data and the rules and then produce an output.  
  - e.g. data + program --> Output

  The success of machine learning algorithms depends heavily on the representation of the data. i.e. The features that are selected.   
  
  But sometimes it's hard to know which features will best contribute to the success of the model.  

  **Representation Learning** is using machine learning to help select the best features.   

Another Solution is to use deep learning. Which can be better at finding abstract high level feautres.   

Deep learning can detect these abstract features by "extracting hidden layers" in the data.   

Deep learning requires lots and lots of data to be more effective than machine learning. And also more processing power. This is why it's popularity has grown so much recently, because more data and faster computers are available.

# Introduction to Deep Learning

Machine learning in a nutshell
  - take a problem
  - find a metric that defines how far away we are from the solution (define the error)
  - minimize the error (gradient descent)

Neural networks
  - We are teaching a computer to split the data. i.e. find what makes one thing different from another.
  - Uses a discrete funciton, so gradient descent is not possible.
  - converting a discrete function to a continuous one by adding a penalty. So basically finding probability of something belonging to a certain class instead of counting how many we got wrong.
  - use something called "maximum likelihood" which is like an error function using probabilities
  - after getting the maximum likelihood you take the logarithm of each probabily is the penalty. 
    - The log of lower probabilities lead to high penalties
    - The sum of these penalties is the loss function

So far this is just explaining logistic regression...   

With neural networks each node is like a probability calculation and the final output of the network is based on all the nodes.   

sooo kind of like a random forest of logistic regressions???



**Activation Function**
  - turns entire number line into a number between 0 and 1 so it's suitable for probability. (1 / 1 + e^-x) called a sigmoid


# Deep learning use cases

- image classification
- object recognition (clarifai)
- video recognition
- speech recognition
- Fact extraction from text
- Translator
- Sentiment analysis (metamind)
- character level text processing
- medical
  - drug discovery
  - radiology
- Finance
- advertising
- fraud detection 
 
