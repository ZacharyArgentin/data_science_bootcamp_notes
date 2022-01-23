# What is an API

- API stands for Application programming interface

- An API is like and instruction manual for how to interact with a web server.

You use an API to figure out what request you want to make to the server, and then the server sends you some information back.

> - Loosely, an API is a programmer friendly version of a website.

**Technical Definition:** An API is the part of the server that receives requests and sends responses.

---

Using APIs helps you utilize third party solutions.
- e.g. If you need weather information you can access an API from a service that provides weather information. You don't have to develop your own weather forecasting service

### Basically:
- an API is just a service provided by a website / company provides purely data responses instead of html responses.
- These responses are usually in JSON or XML format

# XML

xml stands for "extensible markup language"

> - xml tags are not predefined like html tags
> - xml is designed to carry data
> - html is designed for displaying data
> - xml stores data in plain text format, Therefore it is software and hardware independent

# Types of APIs

The classification of API's can be based on 3 parameters
- Ownership type
- Communication level
- Communication type

---

## Ownership Type

- Open API (aka Public API)
  - Anyone can use them
- Partner API
  - Usually associated with a paid service. Need credentials to use them
- Internal API
  - API developed by a company for use within the company
- Composite API
  - Utilizes more than 1 API. 1 request can trigger a request to one of manh other APIs that the composite API is made up of. (I think this is right. The article i was reading was a bit confusing)

---

## Communication level

- High level
- Low level

Like with programming languages, High level APIs are more 'user friendly' at the cost of detailed functionality.

---

## Communication type

- SOAP
- XML-RPC
- JSON-RPC
- REST

---

### SOAP 

- Uses its own protocol called Simple Object Access Protocol
- uses XML
- SOAP has built-in ACID compliance which reduces anomalies and protects the integrity of a database by prescribing exactly how transactions can interact with the database.

SOAP apis are generally more secure and are used for things like banking

---

### XML-RPC

XML-RPC (Extensible markup language – Remote Procedure Calls) is a protocol that uses a specific XML format to transfer data. 

> XML-RPC uses minimum bandwidth and is much simpler and older than SOAP.

---

### JSON-RPC

JSON-RPC (JavaScript Object Notation) is a protocol which uses JSON format to transfer data.

---

### REST

(Representational State Transfer)

- REST apis use URLs and HTTP protocol

- simple to build and scale compared to other types of APIs

- REST APIs facilitates client-server communication with simplicity.

- REST APIs uses SSL security which means it can use HTTPS.

- REST APIs uses different data formats including 
  - plain text
  - HTML
  - XML
  - JSON

  This results in greater browser compatibility

- simple date formats and light payloads

 - REST APIs use a single uniform interface. This simplifies how applications interact with the API by requiring they all interact in the same way, through the same portal. This has advantages and disadvantages.

- REST calls can be cached.

> REST is **Stateless**. Meaning that the server side shouldn't store any information about the session. Every request a client makes should include all the necessary information to understand the request and should not rely on information stored server side.
>
> e.g. cookies store user information on the website. A restful API doesn't store any user information on the website.

# RESTful APIs

This is the most common type of API

> def Client: 
> - The thing accessing the API

> def Resource: 
> - anything the API can provide information about. e.g. images, posts, users

a RESTful api lets you interact with its resources.

> when a RESTful API is called, the server will transfer to the client a representation of the state of the requested resource.

This representation is usually in JSON format



