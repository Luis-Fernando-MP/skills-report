---
title: "securing high concurrency ticket sales microservice"
source_pdf: "bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf"
pdf_path: "bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf"
pages: 35
technique: section-chunks + finding-hooks + es-aliases
enriched_at: 2026-09-06T05:54:12+00:00
---

# securing high concurrency ticket sales microservice

> Fuente PDF: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · técnica **section-chunks + finding-hooks + es-aliases**

## Metadata
- Stem: `securing-high-concurrency-ticket-sales-microservice`
- PDF: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf`
- DOI: `unknown`
- Pages: `35`
- Technique: `section-chunks + finding-hooks + es-aliases`

## Locator index

| Kind | Label | PDF page |
|------|-------|----------|
| abstract | Abstract | 1 |
| finding | Securing High-Concurrency Ticket Sales: A Framework Based on Microservice Zhiyong Zhang*1 … | 1 |
| hallazgo | Securing High-Concurrency Ticket Sales: A Framework Based on microservicio Zhiyong Zhang*1… | 1 |
| concept | Security | ? |
| concept | Microservices | 1 |
| concept | Spring Cloud | 1 |
| concept | High Concurrency | 1 |

## Abstract

Securing High-Concurrency Ticket Sales: A Framework Based on Microservice Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1 1 Hainan University, Haikou, China


## Findings

_Cada ### es un nodo Graphify; el título es el snippet consultable (EN + alias ES)._

### [PDF p.1] Finding: Securing High-Concurrency Ticket Sales: A Framework Based on Microservice Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1 1 Hainan University, Haikou, China
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1**

Securing High-Concurrency Ticket Sales: A Framework Based on Microservice Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1 1 Hainan University, Haikou, China

### [PDF p.1] Hallazgo: Securing High-Concurrency Ticket Sales: A Framework Based on microservicio Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1 1 Hainan University, Haikou, China
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1** · alias ES

Securing High-Concurrency Ticket Sales: A Framework Based on microservicio Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1 1 Hainan University, Haikou, China


## Keywords

### [PDF p.?] Concept: Security
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **?**

### [PDF p.1] Concept: Microservices
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1**

### [PDF p.1] Concepto: microservicios
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1** · alias ES

### [PDF p.1] Concept: Spring Cloud
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1**

### [PDF p.1] Concept: High Concurrency
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1**


## Sections


## Page chunks

_Nodos por página del PDF (acotado)._

### [PDF p.1] Securing High-Concurrency Ticket Sales: A
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **1** / 35

Securing High-Concurrency Ticket Sales: A
                                                      Framework Based on Microservice
                                                              Zhiyong Zhang*1 , Xiaoyan Zhang*1 , and Xiaoqi Li1
                                                                        1
                                                                            Hainan University, Haikou, China




arXiv:2512.24941v2 [cs.SE] 4 Jul 2026
                                        Abstract
                                        The railway ticketing system is one of the most important public service infrastructure.
                                        In peak periods such as holidays, it is often faced with the challenge of high concurrency
                                        scenarios because of a large number of users accessing at the same time. The traditional
                                        aggregation architecture can not meet the peak user requirements because of its insufficient
                                        fault tolerance and low ability. Therefore, the system needs to use microservice architecture
                                        for development, and add multiple security methods to ensure that the system can have
                                        good stability and data consistency under high concurrency scenarios, and can respond
                                        quickly to user requests. This paper introduces the use of B/S architecture and Spring
                                        Cloud to design and develop a railway ticket purchase system that can maintain stability and
                                        reliability under high concurrency scenarios, and formulate multiple security design methods
                                        for the system. This system integrates a range of functions, such as real-time train inquiries,
                                        dynamic seat updates, online seat selection, and ticket purchasing, effectively addressing
                                        common problems associated with offline ticket purchasing, such as long queues and delayed
                                        information. It enables a complete online process from inquiry and booking to payment
                                        and refunds. Furthermore, the ”add passenger” function allows users to purchase tickets for
                                        others, extending the convenience of online ticketing to people with limited internet access.
                                        The system design prioritizes security and stability, while also focusing on high performance,
                                        and achieves these goals through a carefully designed architecture and the integration of
                                        multiple middleware components. After the completion of the system development, the core
                                        interface of the system is tested, and then the results are analyzed. The test data proves
                                        that the system has good ability and stability under high concurrency.

                                        Keywords: Security, Microservices, Spring Cloud, High Concurrency


                                        1 INTRODUCTION
                                             As a critical public service system, the railway ticketing system must handle a massive
                                        volume of daily user requests, especially during peak periods when concurrent access can
                                        reach hundreds of millions of times. The system processes millions of transactions every day,
                                        including not only ticket purchases but also changes and cancellations.


                                        *These authors contributed equally to this work.                                             1
                                        Zhiyong Zhang et al.: Preprint Submitted to Arxiv.

### [PDF p.2] With the rapid popularization of online ticket purchase, more and more users are choos-
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **2** / 35

With the rapid popularization of online ticket purchase, more and more users are choos-
ing to book tickets online, which puts greater pressure on the backend system. The tradi-
tional monolithic system architecture packages all functions together, and when faced with
a large number of users grabbing tickets at the same time, the page often freezes, the oper-
ation is slow, and even the same ticket is sold repeatedly. This paper adopts a microservice
architecture to build the railway ticketing system[3], that is, to split the entire system into
multiple independent modules such as ticket service, payment service, and order service.
Multiple security mechanisms are added to ensure that the system runs smoothly and the
data is not corrupted. Each module can be upgraded and maintained separately, so the over-
all scalability of the system is better. For example, when encountering peak ticket grabbing
during holidays, the number of servers for the ticket service can be increased separately.
Through this distributed deployment and traffic sharing method, the instantaneous high
access volume can be effectively coped with[4].

     The security of a ticketing system is built upon two core requirements: first, the ability
to handle massive user traffic during normal operation, and second, maintaining data con-
sistency across all nodes in the event of unexpected failures[3]. A single error can trigger a
chain reaction of problems. For example, payment failures can lead to duplicate charges or
missed payments, while delays in ticket inventory synchronization can result in overselling.
These risks highlight the importance of building distributed ticketing systems based on a
microservices architecture and rigorously reviewing their security. This is especially crucial
during peak periods such as the annual Spring Festival travel rush, when the system must
reliably support billions of ticket requests daily with near-perfect stability.

     Researchers and practitioners worldwide have made significant progress in the design
and security of railway ticketing systems, particularly through the adoption of microservices
architecture and related protective measures. To cope with peak demand, modern systems
deploy distributed microservices, combined with caching and message queues, to reduce
server load, accelerate response times, and minimize system downtime, ultimately providing
users with a smoother experience[5].

     The application of microservice architecture has been widely validated in major railway
systems worldwide. For example, Amtrak, facing immense access pressure, rebuilt its on-
line ticketing system using a microservice architecture[7], deploying instances through cloud
services and integrating technologies such as API gateways[8] and Spring Cloud[9]. This
transformation significantly improved system stability during peak hours and enhanced the
user experience. Similarly, European railway systems[10], which must handle complex cross-
border, high-concurrency scenarios, have adopted service meshes for service governance and
utilized Kubernetes for containerized management[11].

     This study designed and developed a stable and secure railway ticketing system based
on a microservice architecture. By building an efficient online ticketing platform, it meets
people’s needs for convenient travel, allowing users to complete ticket inquiries, reservations,
payments, and cancellations without leaving home. The system includes functions such as
train schedule inquiry, real-time updates of available tickets, and online seat selection, solving


Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                              2

### [PDF p.3] problems such as long queues and information delays associated with offline ticket purchases.
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **3** / 35

problems such as long queues and information delays associated with offline ticket purchases.
Furthermore, the system adds features such as allowing users to purchase tickets for multiple
passengers, enabling those without internet access to enjoy convenient ticketing services.

     This paper conducts an in-depth study of the system’s backend framework and security
design to ensure system stability, and elaborates on the implementation process of key func-
tional modules. The research includes theoretical analysis, technical design, implementation
of core functions (including security measures), and comprehensive performance testing. In
the system design phase, a system functional requirements structure diagram was designed
based on application needs, technology selection was determined, and a system architecture
diagram was drawn. Simultaneously, the system’s security design scheme was analyzed, a
database E-R diagram was designed, and the data table design was improved based on busi-
ness relationships. In the system implementation phase, the implementation of the main
functional modules is described, the system’s security design scheme is analyzed in detail,
and performance testing was conducted on the system’s core interfaces. The main research
content and innovations of this paper are as follows.

     (1) Design a microservice-based and high-availability traffic control scheme. The sys-
tem, which comprises five modules (membership, ticketing, order, payment, and gateway),
uses Nacos for their management. Furthermore, Sentinel is introduced to achieve precise cir-
cuit breaking, degradation, and interception of abnormal traffic, thereby improving system
availability.

     (2) Implement a packaged cache component library, use Bloom Filter plus Redis to
solve the cache penetration problem, intercept 99% of invalid requests, and reduce the core
interface response time from 200ms to 30ms.

     (3) The algorithm for generating distributed globally unique IDs is optimized by propos-
ing to replace UUID with the Snowflake algorithm, which is customized according to the
specific scenario within the system. This achieves ordered and monotonically increasing ID
generation, is more index-friendly for databases, and improves write performance. Further-
more, tests show that the Snowflake algorithm has better generation performance, higher
uniqueness, and smaller storage space.

     (4) A method is proposed to monitor MySQL’s Binlog logs and then use Canal to cap-
ture data change events in real time. Combined with message queues to trigger asynchronous
cache updates, a highly efficient and reliable database and cache consistency guarantee sys-
tem was constructed. Canal parses the Binlog in Row mode, accurately identifies key oper-
ations such as order status changes and inventory deductions, encapsulates them into JSON
format messages, and sends them to the specified Topic in RocketMQ for asynchronous
processing by consumers.

    (5) By splitting the traditional monolithic architecture, making reasonable technol-
ogy selections and adopting a variety of system stability optimization schemes, this system
can maintain good stability and performance under high concurrency. The core interface
throughput of this system is 817 requests per second and the average response time is 31

Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                         3

### [PDF p.4] milliseconds.
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **4** / 35

milliseconds.

2 BACKGROUND
2.1 Microservices
(1) Spring

     The Spring framework[12] is the basic architecture for Java enterprise application de-
velopment. Its core principle is based on the two major features of inversion of control and
dependency injection. It manages components through the Core Container, which means
that after correct configuration, the container will obtain the right to create instance objects
and then automatically inject them when needed. At the same time, it separates cross-
cutting concerns[13] by means of aspect-oriented programming. For example, logging and
transactions are implemented in a non-intrusive way through aspect-oriented programming.
Its modular design covers sub-projects such as Spring MVC[14], Spring Data and Spring
Security. Although Spring is a lightweight container, the complexity of the project is high
because explicit configuration is required in XML or using Java annotations before develop-
ing business code. Therefore, the requirements for developers are very high. Figure 2.1 is
the architecture diagram of the Spring framework.




                     Figure 2.1: Spring Framework Architecture Diagram

(2)Spring Boot

     The Spring framework[15] requires a lot of configuration, which can easily lead to various
exceptions and low development efficiency. Spring Boot adopts the concept of ”convention
over configuration” and optimizes the conventional development model. Its core technologies
include an auto-wiring mechanism based on conditional configuration, starter dependencies
for standardized dependency management, and embedded Servlet containers (such as Tom-
cat/Jetty).

Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                            4

### [PDF p.5] Auto-configuration is the core function of the Spring Boot framework. After importing
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **5** / 35

Auto-configuration is the core function of the Spring Boot framework. After importing
the corresponding dependency resource package using a dependency management tool such
as Maven[16], it can be managed through auto-configuration. Figure 2.2 shows the execution
flowchart of the Spring Application.




                      Figure 2.2: Spring Application Execution Flowchart



     This framework significantly lowers the barrier to entry for Spring applications by sim-
plifying environment configuration and reducing boilerplate code. It also adapts to the
microservice architecture requirements of the cloud-native era, becoming the mainstream
industry standard for rapidly building production-grade applications and demonstrating sig-
nificant engineering value in DevOps and continuous integration scenarios.

(3) Microservice Decomposition Based on Spring Boot

    Traditional monolithic architecture integrates various business functions into a single
project and deploys them in a unified package. Complex application architecture can lead to
poor system availability and impact system performance. Figure 2.3 illustrates a traditional
monolithic architecture.

Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                         5

### [PDF p.6] Figure 2.3: Schematic Diagram of Monolithic Architecture
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **6** / 35

Figure 2.3: Schematic Diagram of Monolithic Architecture

     Microservice architecture[17] is a set of best practice solutions guided by the service-
oriented approach. It is not a framework itself, but a software architecture style. It is based
on many small projects with single functions and responsibilities. By combining them, a
complex large application can be realized. Service-oriented architecture is to break down
the functional modules in the monolithic architecture into multiple independent projects.
Figure 2.4 is a schematic diagram of microservice architecture.




                 Figure 2.4: Schematic Diagram of Microservice Architecture

     Although microservice architecture can improve system availability[18], it also brings


Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                           6

### [PDF p.7] many problems such as how services can make remote calls, how configurations can be uni-
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **7** / 35

many problems such as how services can make remote calls, how configurations can be uni-
formly managed, and how applications can monitor traffic. To solve these problems, Spring
Cloud Alibaba technology, which is based on the Spring Cloud software architecture style
and includes multiple core components, can be used. For example, Nacos can register ser-
vices and configurations on the server and then manage them, Sentinel can restrict external
traffic from entering the system, and RocketMQ can process distributed messages, which
helps developers quickly build Java applications with strong availability and good scalabil-
ity. Spring Cloud Alibaba[19] is compatible with Spring Cloud[20] native components such
as OpenFeign and Gateway, which greatly simplifies the workload of developers and has
become a popular choice for enterprise-level microservice development. As shown in Figure
2.5, Spring Cloud Alibaba integrates various functional components and implements auto-
matic assembly of these components based on Spring Boot, providing a good out-of-the-box
experience[20].




   Figure 2.5: Schematic diagram of Spring Cloud Microservice Functional Components

2.2 Database
(1) MySQL persistent layer database

     MySQL[22] is an open-source relational database management system that uses SQL
statements to store data in a table structure and supports complex transaction processing
and relational queries. Its core features include transaction support, data persistence, and
scalability such as support for master-slave replication, database sharding and table parti-
tioning, and read-write separation. These core features are the basis for its ability to cope
with high concurrency scenarios[23].

(2) Redis cache database

    Redis is a high-performance in-memory key-value database[23] that responds to read
and write operations with extremely low latency. As shown in Figure 2.6, the key is a string


Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                         7

### [PDF p.8] type, while the value supports a variety of data types[25].
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **8** / 35

type, while the value supports a variety of data types[25].




                                  Figure 2.6: Redis Data Types

     Redis is used as a caching layer to intercept high-frequency requests and reduce the
load on the MySQL database. The MySQL database serves as the persistent layer for core
data storage (as shown in Figure 2.7). This combination fully leverages MySQL’s strong
consistency and Redis’s high performance to build a reliable and responsive application
system[25].




Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                     8

### [PDF p.9] Figure 2.7: Schematic Diagram of MySQL and Redis Collaboration
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **9** / 35

Figure 2.7: Schematic Diagram of MySQL and Redis Collaboration

2.3 Canal monitoring
    Canal is middleware used for real-time monitoring of database log changes. It parses
MySQL’s Binlog logs and efficiently pushes change events to downstream systems, such as
caches, message queues, and big data platforms, thereby achieving real-time synchronization
between databases and heterogeneous data sources[27].

    Canal acts as a MySQL replica, reading and parsing the master’s Binlog logs to capture
data changes. It supports full and incremental synchronization, and is suitable for scenarios
such as heterogeneous data replication, cache updates, real-time analysis, and cross-data
center synchronization. Canal features low invasiveness, high real-time performance, and
high availability, and can be seamlessly integrated with systems such as Kafka, RocketMQ,
and Elasticsearch. It is an important tool for building real-time data pipelines[27] and
ensuring data consistency. Figure 2.8 illustrates its working principle.




                  Figure 2.8: Schematic Diagram of Canal Working Principle

2.4 Algorithms
(1) AES

    This system uses the AES encryption algorithm and the ShardingSphere framework
to implement data encryption. The AES encryption process can be divided into several
rounds, each encompassing four main steps: SubBytes, ShiftRows, MixColumns, and Ad-
dRoundKey. The encryption process begins with an initial round key addition, followed by N
rounds (which determined by the key length) of operations including SubBytes, ShiftRows,
MixColumns, and AddRoundKey. However, the final round only requires the first three


Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                         9

### [PDF p.10] M is the initial plaintext, K 0 is the starting key, and C 0 is obtained by performing the
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **10** / 35

steps.

   M is the initial plaintext, K 0 is the starting key, and C 0 is obtained by performing the
AddRoundKey operation on the initial plaintext, as shown in Formula 2-1.


                                           C0 = M ⊕ K0                                  (2-1)


     In each round of encryption, SubBytes byte substitution is performed first, then row
shifting is achieved through ShiftRows, followed by column obfuscation transformation through
the MixColumns step. Finally, the result of that round is generated by XORing the round
key with the AddRoundKey operation. As shown in Formula 2-2, the result after the i-th
round of encryption is C i, the key used in the i-th round is K i.

                                                              
                      Ci =   Ci−1 −−−−−→ ShiftRows −−−−−−−→ ⊕ Ki                        (2-2)
                                     SubBytes              MixColumns


     As shown in Formula 2-3, C N is the final output ciphertext.

                                                      
                                        SubBytes
                            CN = CN −1 −−−−−→ ShiftRows ⊕ KN                            (2-3)

     SubBytes performs S-Box permutation on each byte as shown in Formula 2-4.


                                  b′ = S-Box(b) (1 ≤ b ≤ 256)                           (2-4)

     MixColumns matrix operations (finite field GF(28 )) are shown in Formula 2-5.

                                 ′                           
                                 c0      02      03   01   01      c0
                                c′1   01      02   03   01 c1 
                                                                 
                                 ′ = 
                                c2   01                      ×                      (2-5)
                                                 01   02   03 c2 
                                 c′3     03      01   01   02      c3

     The coefficients 02, 03, and 01 are hexadecimal polynomials in GF(28 ). The multiplica-
tion rule here is finite field multiplication, and the addition rule uses the XOR operation.

    The ⊕ symbol in Formula 2-6 indicates that the operation is performed according to
the byte XOR rule, that is, the state matrix and AddRoundKey are XORed by bytes, as
shown in Formula 2-6.


                                   State = State ⊕ RoundKey                             (2-6)

Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                        10

### [PDF p.11] (2) Customizable Snowflake Algorithm
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **11** / 35

(2) Customizable Snowflake Algorithm

    There are many scenarios in distributed systems where globally unique IDs are used.
To avoid ID conflicts, the Snowflake algorithm can be used[29]. The algorithm generates
auto-incrementing long values with customizable lengths, and the ordered auto-incrementing
characteristic ensures high performance of B+ Tree index insertion in MySQL[29]. The
Snowflake structure is shown in Figure 2.9.




                      Figure 2.9: Snowflake Algorithm Structure Diagram

     The Snowflake algorithm is composed of four parts. The first part is the sign bit,
occupying 1 bit. The second part is the timestamp, which uses 41 bits. The third part is
the identifier bit, comprising 10 bits in total, with 5 bits allocated to the datacenterId and
the other 5 bits to the workerId. These two identifiers are usually combined to represent
different deployment nodes. The fourth part is the sequence number, which occupies 12 bits.
Because the sequence number is monotonically increasing, it can ensure that the Snowflake
algorithm generates globally unique IDs[37]. Then, when the timestamp is fixed, 212 unique
IDs can be generated per second.

     The Snowflake generation formula is based on the OR operation of the displacements
of each part, as shown in Formula 2-7.

                                                                           
                  long id = (timestamp − twepoch) ≪ timestampLeftShift
                                                             
                           | datacenterId ≪ datacenterIdShift
                                                                                        (2-7)
                           | workerId ≪ workerIdShift
                           | sequence


   The parameter twepoch represents the custom epoch start time. The parameter times-
tampLeftShift indicates the number of bits for the timestamp left shift. The parameter


Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                         11

### [PDF p.12] datacenterIdShift defines the number of bits for the datacenter ID left shift. The parameter
- Locator: `bibliography/auto/pdfs/securing-high-concurrency-ticket-sales-microservice.pdf` · página **12** / 35

datacenterIdShift defines the number of bits for the datacenter ID left shift. The parameter
workerIdShift specifies the number of bits for the worker machine ID left shift. Finally, the
parameter sequence denotes the auto-incrementing sequence within the current millisecond.

(3) Bloom Filter

     Bloom Filter utilize bit arrays and multiple hash functions to achieve fast member
lookup, making them an efficient and reliable data structure[29]. The working principle
of a Bloom Filter is usually to use a binary array to represent a set, with all data in the
array initially set to 0. Then, for each element to be added to the container, multiple hash
values are calculated using multiple hash functions, and the corresponding positions in the
bit array are set to 1. When determining whether an element exists in the container, the
element also calculates its corresponding hash value using multiple hash functions, and then
checks whether the data stored in the corresponding positions in the bit array are both 1.
If both are 1, since hash collisions may occur, the element may only exist in the container,
and further querying of the underlying data storage container is needed to confirm whether
it really exists[31]. However, if any position is 0, it means that the element definitely does
not exist in the container. The principle diagram is shown in Figure 2.10.




                       Figure 2.10: Schematic Ciagram of a Bloom Filter

       The formula for calculating the false positive rate of a Bloom Filter is shown in Formula
2-8.

                                                 kn κ
                                                  
                                          p ≈ 1−em                                         (2-8)

     The core parameters are the number of elements n, the size of the binary array m, and
the number of hash functions k. Therefore, the required binary array size m for calculating
the false positive rate can be derived as shown in Formula 2-9.

Zhiyong Zhang et al.: Preprint Submitted to Arxiv.                                           12

_… 23 páginas más en el PDF (no indexadas como chunks)._
