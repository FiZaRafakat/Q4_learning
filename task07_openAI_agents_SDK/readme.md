# Task 06 

# Task 06 – OpenAI Agents SDK

Well, Task 06 is about answering the following questions:

#### 1. The `Agent` class has been defined as a `dataclass`. Why?

#### 2a. The system prompt is contained in the `Agent` class as `instructions`. Why? And why can you also set it as a callable?

#### 2b. The user prompt is passed as a parameter in the `run` method of `Runner`, and the method is a `@classmethod`. Why?

#### 3. What is the purpose of the `Runner` class?

#### 4. What are generics in Python? Why do we use them for `TContext`?

---

But before answering these questions, we have to understand some key concepts.

## 📘 What I Covered in My Blog

To build a solid foundation, here’s what I understood and covered in my blog in bullet points:

- What the OpenAI Agents SDK is and what it enables
- Key components: Agent, Runner, Tools, Handoffs, Guardrails, Tracing, and Streaming
- The Agent loop and how it handles input, tool calls, handoffs, and responses
- Building multi-turn conversations using `RunResult.to_input_list()`
- How to customize agent behavior using `run_config`
- The difference between Streaming and Tracing
- How everything works together: agents think, tools act, runners manage

---

To understand all these basics, I first read the article:  
👉 [OpenAI Agents SDK review](https://medium.com/@danushidk507/openai-agents-sdk-ii-15a11d48e718)

**This blog helped me understand the core SDK concepts.**

Then, I wrote my own blog based on what I learned:  
👉 [OpenAI Agents SDK: The Complete Beginner’s Guide](https://medium.com/@fizarafakat/openai-agents-sdk-the-complete-beginners-guide-ba531871c9b2)

Now let’s jump into answering the task questions above.


## 1. The Agent class has been defined as a dataclass — why?

Imagine you want to create a blueprint for an "Agent" — like a little robot that follows instructions. This blueprint needs to store some information about the agent, like its name, role, or maybe some instructions it follows.

A dataclass in Python is a special way to create such blueprints easily. It automatically gives you some handy features, like:

- Automatically creating an initializer (__ init__) method so you don't have to write it yourself.

- Automatically creating a nice representation of the object when you print it.

- Makes your code cleaner and easier to read.

### So, why use a dataclass for the Agent?

Because the Agent is mostly just a container to hold data (like instructions, name, role). The dataclass makes it simple to create and use these containers without writing extra code.

Example:

    from dataclasses import dataclass

    @dataclass
    class Agent:
        name: str
        role: str
        instructions: str

    Now, when you create an agent:

    agent = Agent(name="HelperBot", role="Assistant", instructions="Always be polite")
    print(agent)

You get:

`Agent(name='HelperBot', role='Assistant', instructions='Always be polite')`

No extra work needed!

## 2a. The system prompt is contained in the Agent class as instructions? Why you can also set it as callable?

The system prompt is like the main instruction or the "personality" of the agent. For example, it might say: "You are a helpful assistant who explains things clearly."

We put it inside the Agent class as instructions because the agent needs this info to know how to behave — it’s part of the agent's identity.

But sometimes, the instructions might not be fixed — maybe they depend on something dynamic, like the current time or a user’s preference.

That’s why we can also make the system prompt callable — meaning it’s a function that runs when needed and returns the instructions.

Example:

    def dynamic_instructions():
        return "You are an assistant who adjusts answers based on the user's mood."

    agent = Agent(name="MoodBot", role="Helper", instructions=dynamic_instructions)

Here, instead of a fixed string, instructions is a function. When you want to get the instructions, you call it:

`print(agent.instructions())  # Runs the function to get instructions`

This adds flexibility — the agent can change how it behaves based on different situations.

## 2b. But the user prompt is passed as a parameter in the run method of Runner, and the method is a classmethod. Why?

Let’s first break this down.

- The user prompt is the input or question that a user gives to the agent, like “Explain Python dataclasses.”

- The Runner class is the one in charge of actually running or executing the agent’s logic — think of it as the "engine" that makes the agent work.

- The run method is a classmethod, which means it belongs to the class itself, not a specific instance (object).

### Why do we pass the user prompt to run as a parameter?

Because the user’s input changes every time. The Runner doesn’t hold the user prompt inside itself — it just needs the prompt each time it runs. This keeps the runner reusable and flexible, able to work with any user prompt without storing it permanently.

### Why is run a classmethod?

Because sometimes you don’t want to create a new instance of Runner every time you want to run it. Using a classmethod allows you to call `Runner.run(user_prompt)` directly on the class without creating an object. This is simple and efficient.

## 3. What is the purpose of the Runner class?

Think of the Runner as the boss or conductor in an orchestra.

- The Agent holds all the information and instructions.

- The Runner is the one who takes the user’s input and the agent’s instructions and orchestrates the whole process.

- It calls the agent’s logic with the input.

- It manages the flow — how the input is processed and the output is created.

- It can also handle extra steps like logging, error checking, or managing state if needed.

Without the Runner, the Agent just sits there with its instructions. The Runner makes the magic happen by running the agent.

## 4. What are generics in Python? Why do we use it for TContext?

**Generics** are like placeholders in your code that allow you to write flexible, reusable code. Imagine you want to create a box that can hold anything: apples, toys, or books. Instead of creating a new box for each item, you create one generic box that can hold any type.

In Python, **generics** let you write functions or classes that work with any type, but still keep track of what type it is. This helps avoid mistakes and makes your code safer.

**TContext** is a type variable — a placeholder for the type of context (extra data or environment) your program might work with.

### Why use generics for TContext?

Because the Runner or Agent might work with different kinds of contexts — maybe sometimes it’s just a dictionary, sometimes it’s a custom object with special data.

By using a generic TContext, you tell Python:
_**“This part of the code works with any type of context you want, but keep it consistent.”**_

This makes your code more reusable and easier to maintain.

Example:

    from typing import TypeVar, Generic

    TContext = TypeVar('TContext')

    class Runner(Generic[TContext]):
        def run(self, context: TContext):
            print(f"Running with context: {context}")

Now, you can create a Runner that works with any type of context:

    runner1 = Runner[str]()
    runner1.run("A simple string context")

    runner2 = Runner[dict]()
    runner2.run({"key": "value"})



_Happy Coding 🌸_