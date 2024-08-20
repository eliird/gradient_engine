# Gradient Engine for Backpropogation

## Motivation

To visualize the backpropogation process.

## Installation

> git clone https://github.com/eliird/gradient_engine
> pip install -e .


# Usage


```
from gradient_engine import Neuron, Layer, MLP, Value, draw_dot

# the code below evaluates the expression f = a * b + c

a = Value(2.0)
b = Value(3.0)

c = Value(5.0)

d = a * b
e = d + c
f = e.tanh()


# graph of the computation can be visualized using draw_dot function
# check notebook for example
draw_dot(f)

# gradients can be computed using the backward function
f.backward() 
draw_dot(f)
```

`nn.py` contains the implementation of a single `neuron`, a single `layer` and an `MLP`
```
# Neuron
x = [2, 0]
n = Neuron(n_in=2) # n_in specifies the amount of inputs to the neuron
out = n(x)
print(n.parameters())
out.backward()
draw_dot(out)

# Layer
x = [2, 0]
n = Layer(n_in=2, n_out=4) # layer takes input and output dimension
out = n(x)
out.backward()
draw_dot(out)

# MLP
x = [2.0, 3.0, -1.0]
n = MLP([3, 4, 2, 1]) # creates a NN with the shape of 3, 4, 2, 1
out = n(x)
out.backward()
draw_dot(out)
```


# Training a dummy neural network

```
model = MLP([3, 4, 2, 1])

# creating the dummy dataset
xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0]
]

ys = [1.0, -1.0, -1.0, 1.0]
y_pred = [model(x) for x in xs]
print("Predictions Before training: ", y_pred)


# training loop
train_loss = []
lr = 1e-3

for i in range(3000):
    # forward pass
    y_pred = [model(x) for x in xs]
    loss = [(y_out - ygt)**2 for ygt, y_out in zip(ys, y_pred)]
    loss = sum(loss)
    
    # zero out the grads
    for p in model.parameters():
        p.grad = 0.0
        
    # backward pass
    loss.backward()
    train_loss.append(loss.data)
    
    # update the gradients
    for p in model.parameters():
        p.data += lr * (-p.grad)


# plot the loss for the traininig
plt.plot(train_loss)
plt.xlabel("num_of_pass")
plt.ylabel("MSE Loss")
print("Preds after training:", y_pred)
plt.show()
```


