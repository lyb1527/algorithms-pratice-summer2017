###编程常见问题:

Write a function to reverse a string.
Write function to compute fibonacci number.
Write a function to reverse a string.
Write a function to find a string length.
Determine whether an integer is a palindrome.
Determine whether a string is a palindrome.
Implement regular expression matching with support for ‘.’ and ‘*’.
Merge two sorted linked lists and return it as a new list.
Write a function to determine if a given target is in the array.
Given a binary tree, determine if it is height-balanced.
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Implement wildcard pattern matching
Given a string, find the length of the longest substring without repeating characters.
Implement atoi to convert a string to an integer.
Given a sorted array, remove the duplicates in place such that each element appear only once and
return the new length.
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
Given a sorted linked list, delete all duplicates such that each element appear only once
Given a binary tree, determine if it is a valid binary search tree (BST).

Given a binary tree, return the inorder traversal of its nodes' values iteratively without using recursion.
Given inorder and postorder traversal of a tree, construct the binary tree.
Output all prime numbers up to a specified integer n.
Given a binary tree, find the lowest common ancestor of two given nodes in the tree.
Given preorder and inorder traversal of a tree, construct the binary tree.


###面向对象的常见问题
Design a deck of cards that can be used for card game applications.
Design a parking lot.
Create a class design to represent a system.
Design an OO representation for given object.


###脚本和正则表达式的常见问题
How do you take a single line of input from the user in a shell script?
Write a script to convert all DOS style backslashes to UNIX style slashes in a list of files.
Write a regular expression (or sed script) to replace all occurrences of the letter ‘f’, followed by any
number of characters, followed by the letter ‘a’, followed by one or more numeric characters, followed
by the letter ‘n’, and replace what’s found with the string “UNIX”.
What happens to a child process that dies and has no parent process to wait for it and what’s bad about
this?
How do you create a swapfile?1. How do you take a single line of input from the user in a shell script?


数据结构常见问题以及解答(基础书本知识,知识来源 google)
1) What is data structure?
Data structure refers to the way data is organized and manipulated. It seeks to find ways to make
data access more efficient. When dealing with data structure, we not only focus on one piece of
data, but rather different set of data and how they can relate to one another in an organized
manner.

2) Differentiate file structure from storage structure.
Basically, the key difference is the memory area that is being accessed. When dealing with the
structure that resides the main memory of the computer system, this is referred to as storage
structure. When dealing with an auxiliary structure, we refer to it as file structure.

3) When is a binary search best applied?
A binary search is an algorithm that is best applied to search a list when the elements are already
in order or sorted. The list is search starting in the middle, such that if that middle value is not the
target search key, it will check to see if it will continue the search on the lower half of the list or
the higher half. The split and search will then continue in the same manner.

5) How do you reference all the elements in a one-dimension array?
To do this, an indexed loop is used, such that the counter runs from 0 to the array size minus one.
In this manner, we are able to reference all the elements in sequence by using the loop counter as
the array subscript.

6) In what areas do data structures applied?
Data structure is important in almost every aspect where data is involved. In general, algorithms
that involve efficient data structure is applied in the following areas: numerical analysis,
operating system, A.I., compiler design, database management, graphics, and statistical analysis,
to name a few.

7) What is LIFO?
LIFO is short for Last In First Out, and refers to how data is accessed, stored and retrieved.
Using this scheme, data that was stored last , should be the one to be extracted first. This also
means that in order to gain access to the first data, all the other data that was stored before this
first data must first be retrieved and extracted.

8 ) What is a queue?
A queue is a data structure that can simulates a list or stream of data. In this structure, new
elements are inserted at one end and existing elements are removed from the other end.

9) What are binary trees?
A binary tree is one type of data structure that has two nodes, a left node and a right node. In
programming, binary trees are actually an extension of the linked list structures.

10) Which data structure is applied when dealing with a recursive function?
Recursion, which is basically a function that calls itself based on a terminating condition, makes
use of the stack. Using LIFO, a call to a recursive function saves the return address so that it
knows how to return to the calling function after the call terminates.


11) What is a stack?
A stack is a data structure in which only the top element can be accessed. As data is stored in the
stack, each data is pushed downward, leaving the most recently added data on top.

12) Explain Binary Search Tree
A binary search tree stores data in such a way that they can be retrieved very efficiently. The left
subtree contains nodes whose keys are less than the node’s key value, while the right subtree
contains nodes whose keys are greater than or equal to the node’s key value. Moreover, both
subtrees are also binary search trees.

13) What are multidimensional arrays?
Multidimensional arrays make use of multiple indexes to store data. It is useful when storing data
that cannot be represented using a single dimensional indexing, such as data representation in a
board game, tables with data stored in more than one column.

14) Are linked lists considered linear or non-linear data structure?
It actually depends on where you intend to apply linked lists. If you based it on storage, a linked
list is considered non-linear. On the other hand, if you based it on access strategies, then a linked
list is considered linear.

15) How does dynamic memory allocation help in managing data?
Aside from being able to store simple structured data types, dynamic memory allocation can
combine separately allocated structured blocks to form composite structures that expand and
contract as needed.

16) What is FIFO?
FIFO is short for First-in, First-out, and is used to represent how data is accessed in a queue.
Data has been inserted into the queue list the longest is the one that is removed first.

17) What is an ordered list?
An ordered list is a list in which each node’s position in the list is determined by the value of its
key component, so that the key values form an increasing sequence, as the list is traversed.

18) What is merge sort?
Merge sort takes a divide-and-conquer approach to sorting data. In a sequence of data, adjacent
ones are merged and sorted to create bigger sorted lists. These sorted lists are then merged again
to form an even bigger sorted list, which continuous until you have one single sorted list.

19) Differentiate NULL and VOID.
Null is actually a value, whereas Void is a data type identifier. A variable that is given a Null
value simply indicates an empty value. Void is used to identify pointers as having no initial size.

20) What is the primary advantage of a linked list?
A linked list is a very ideal data structure because it can be modified easily. This means that
modifying a linked list works regardless of how many elements are in the list.

21) What is the difference between a PUSH and a POP?
Pushing and popping applies to the way data is stored and retrieved in a stack. A push denotes
data being added to it, meaning data is being “pushed” into the stack. On the other hand, a pop
denotes data retrieval, and in particular refers to the topmost data being accessed.

22) What is a linear search?
A linear search refers to the way a target key is being searched in a sequential data structure.
Using this method, each element in the list is checked and compared against the target key, and
is repeated until found or if the end of the list has been reached.

23) How does variable declaration affect memory allocation?
The amount of memory to be allocated or reserved would depend on the data type of the variable
being declared. For example, if a variable is declared to be of integer type, then 32 bits of
memory storage will be reserved for that variable.

24) What is the advantage of the heap over a stack?
Basically, the heap is more flexible than the stack. That’s because memory space for the heap
can be dynamically allocated and de-allocated as needed. However, memory of the heap can at
times be slower when compared to that stack.

25) What is a postfix expression?
A postfix expression is an expression in which each operator follows its operands. The advantage
of this form is that there is no need to group sub-expressions in parentheses or to consider
operator precedence.

26) What is Data abstraction?
Data abstraction is a powerful tool for breaking down complex data problems into manageable
chunks. This is applied by initially specifying the data objects involved and the operations to be
performed on these data objects without being overly concerned with how the data objects will
be represented and stored in memory.

27) How do you insert a new item in a binary search tree?
Assuming that the data to be inserted is a unique value (that is, not an existing entry in the tree),
check first if the tree is empty. If it’s empty, just insert the new item in the root node. If it’s not
empty, refer to the new item’s key. If it’s smaller than the root’s key, insert it into the root’s left
subtree, otherwise, insert it into the root’s right subtree.

28) How does a selection sort work for an array?
The selection sort is a fairly intuitive sorting algorithm,, though not necessarily efficient. To
perform this, the smallest element is first located and switched with the element at subscript zero,
thereby placing the smallest element in the first position. The smallest element remaining in the
subarray is then located next with subscripts 1 through n-1 and switched with the element at
subscript 1, thereby placing the second smallest element in the second position. The steps are
repeated in the same manner till the last element.

29) How do signed and unsigned numbers affect memory?
In the case of signed numbers, the first bit is used to indicate whether positive or negative, which
leaves you with one bit short. With unsigned numbers, you have all bits available for that number.
The effect is best seen in the number range (unsigned 8 bit number has a range 0-255, while 8-bit
signed number has a range -128 to +127.

30) What is the minimum number of nodes that a binary tree can have?
A binary tree can have a minimum of zero nodes, which occurs when the nodes have NULL
values. Furthermore, a binary tree can also have 1 or 2 nodes.

31) What are dynamic data structures?
Dynamic data structures are structures that expand and contract as a program runs. It provides a
flexible means of manipulating data because it can adjust according to the size of the data.

32) In what data structures are pointers applied?
Pointers that are used in linked list have various applications in data structure. Data structures
that make use of this concept include the Stack, Queue, Linked List and Binary Tree.

33) Do all declaration statements result in a fixed reservation in memory?
Most declarations do, with the exemption of pointers. Pointer declaration does not allocate
memory for data, but for the address of the pointer variable. Actual memory allocation for the
data comes during run-time.

34) What are ARRAYs?
When dealing with arrays, data is stored and retrieved using an index that actually refers to the
element number in the data sequence. This means that data can be accessed in any order. In
programming, an array is declared as a variable having a number of indexed elements.

35) What is the minimum number of queues needed when implementing a priority queue?
The minimum number of queues needed in this case is two. One queue is intended for sorting
priorities while the other queue is intended for actual storage of data.

36) Which sorting algorithm is considered the fastest?
There are many types of sorting algorithms: quick sort, bubble sort, balloon sort, radix sort,
merge sort, etc. Not one can be considered the fastest because each algorithm is designed for a
particular data structure and data set. It would depend on the data set that you would want to sort.

37) Differentiate STACK from ARRAY.
Data that is stored in a stack follows a LIFO pattern. This means that data access follows a
sequence wherein the last data to be stored will the first one to be extracted. Arrays, on the other
hand, does not follow a particular order and instead can be accessed by referring to the indexed
element within the array.

38) Give a basic algorithm for searching a binary search tree.
1. if the tree is empty, then the target is not in the tree, end search
2. if the tree is not empty, the target is in the tree
3. check if the target is in the root item
4. if target is not in the root item, check if target is smaller than the root’s value
5. if target is smaller than the root’s value, search the left subtree
6. else, search the right subtree

39) What is a dequeue?
A dequeue is a double-ended queue. This is a structure wherein elements can be inserted or
removed from either end.

40) What is a bubble sort and how do you perform it?
A bubble sort is one sorting technique that can be applied to data structures such as an array. It
works by comparing adjacent elements and exchanges their values if they are out of order. This
method lets the smaller values “bubble” to the top of the list, while the larger value sinks to the
bottom.

41) What are the parts of a linked list?
A linked list typically has two parts: the head and the tail. Between the head and tail lie the actual
nodes, with each node being linked in a sequential manner.

42) How does selection sort work?
Selection sort works by picking the smallest number from the list and placing it at the front. This
process is repeated for the second position towards the end of the list. It is the simplest sort
algorithm.

43) What is a graph?
A graph is one type of data structure that contains a set of ordered pairs. These ordered pairs are
also referred to as edges or arcs, and are used to connect nodes where data can be stored and
retrieved.

44) Differentiate linear from non linear data structure.
Linear data structure is a structure wherein data elements are adjacent to each other. Examples of
linear data structure include arrays, linked lists, stacks and queues. On the other hand, non-linear
data structure is a structure wherein each data element can connect to more than two adjacent
data elements. Examples of non linear data structure include trees and graphs.

45) What is an AVL tree?
An AVL tree is a type of binary search tree that is always in a state of partially balanced. The
balance is measured as a difference between the heights of the subtrees from the root. This selfbalancing
tree was known to be the first data structure to be designed as such.

46) What are doubly linked lists?
Doubly linked lists are a special type of linked list wherein traversal across the data elements can
be done in both directions. This is made possible by having two links in every node, one that
links to the next node and other one that links to the previous node.

47) What is Huffman’s algorithm?
Huffman’s algorithm is associated in creating extended binary trees that has minimum weighted
path lengths from the given weights. It makes use of a table that contains frequency of
occurrence for each data element.

48) What is Fibonacci search?
Fibonacci search is a search algorithm that applies to a sorted array. It makes use of a divide-andconquer
approach that can greatly reduce the time needed in order to reach the target element.

49) Briefly explain recursive algorithm.
Recursive algorithm targets a problem by dividing it into smaller, manageable sub-problems. The
output of one recursion after processing one sub-problem becomes the input to the next recursive
process.

50) How do you search for a target key in a linked list?
To find the target key in a linked list, you have to apply sequential search. Each node is traversed
and compared with the target key, and if it is different, then it follows the link to the next node.
This traversal continues until either the target key is found or if the last node is reached.



####非技术类型的常见问题:

What are you looking for in your next job? What is important to you?
更多的技术挑战;你们公司的技术和项目;对个人最重要的是高质量的产品;和家庭生活;

What is your greatest weakness?
对于这个这个陷阱问题，可以用如下几种方式: 1.分析职位所需技能，然后诚实的告知面试官希望
更多地在你公司获取某种体验.2.转化话题为上一个工作中，你有什么提高的，从而告知面试官你
怎么从过去的经验获取进步.3.尽量把负面的转化成正面,比如你可以说，你总是对项目的完成很有
紧迫感.
样本答案:
1. 我在工作在每一个项目的时候，我更喜欢在最后期限之前就完成
2. 我可能不擅长组织多个项目，但是我用一个时间管理系统极大的帮助和改善了自己的这个问
题
3. 我以前总是在最后时刻才去规划下一周的事情，我现在习惯了提前规划
4. 我过于追求完美.
5. 我过去总是习惯于一次只完成一个项目，现在我尝试和习惯了在一个时间内完成多个项目.

What is your greatest strength?
1. 技术能力
2. 合作能力
3. 项目时间管理能力

Describe a typical work week.
1. 计划新的项目
2. 总结上一周得失
3. 分析可能问题和障碍
4. 和组员以及管理者交流
5. 项目研发

How would you describe the pace at which you work?
1. 充满挑战
2. 快速的进展
3. 准确的分析

How do you handle stress and pressure?
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
1. 散步
2. 深度分析压力来源
3. 和同事交流

What motivates you?
1. 热爱编程
2. 热爱项目
3. 对公司有爱

Tell me about yourself.
1. 有技术
2. 善于合作
3. 敢于承担责任

Questions about your career goals.
1. 成为该领域的专家
2. 帮助公司在这方面有所提高
3. 减少花费增加效率

What type of work environment do you prefer?
1. 有活力
2. 有挑战
3. 和谐相处

##想要在电话面试中表现出色，以下有一些好建议：
 Do:
 你应该这么做：
 1.Prepare yourself for the call as you would for a face-to-face interview.
 你怎么准备“面对面”面试的，就怎么准备电话面试。
 2.Choose a quiet place to take the call, with no risk of interruption or background noise.
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
 找一个安静的地方接受电话面试，确保不会被打断，也不要有背景杂音。
 3.Pay as much attention to listening as to speaking.
 听清楚问题和好好回答问题一样重要。
 4.Call from a landline to minimise the chance of interference or lost connection.
 用固定电话进行电话面试，以避免发生信号中断或信号干扰。
 5.Take things slowly –there is no need to rush.
 慢慢来，没有什么事需要你急着去做的。




 ##Network related topics
 1. What are 10Base2, 10Base5 and 10BaseT Ethernet LANs
10Base2—An Ethernet term meaning a maximum transfer rate of 10 Megabits per second
that uses baseband
signaling, with a contiguous cable segment length of 100 meters and a maximum of 2
segments.
10Base5—An Ethernet term meaning a maximum transfer rate of 10 Megabits per second
that uses baseband
signaling, with 5 continuous segments not exceeding 100 meters per segment.
10BaseT—An Ethernet term meaning a maximum transfer rate of 10 Megabits per second
that uses baseband
signaling and twisted pair cabling.
2. What is the difference between an unspecified passive open and a fully specified passive
open
An unspecified passive open has the server waiting for a connection request from a client. A
fully specified passive open has the server waiting for a connection from a specific client.
3. Explain the function of Transmission Control Block
A TCB is a complex data structure that contains a considerable amount of information about
each connection.
4. What is a Management Information Base (MIB)
A Management Information Base is part of every SNMP-managed device. Each SNMP agent
has the MIB database that contains information about the device's status, its performance,
connections, and configuration. The MIB is queried by SNMP.
5. What is anonymous FTP and why would you use it
Anonymous FTP enables users to connect to a host without using a valid login and password.
Usually, anonymous FTP uses a login called anonymous or guest, with the password usually
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
requesting the user's ID for tracking purposes only. Anonymous FTP is used to enable a large
number of users to access files on the host without having to go to the trouble of setting up
logins for them all. Anonymous FTP systems usually have strict controls over the areas an
anonymous user can access.
6. What is a pseudo tty
A pseudo tty or false terminal enables external machines to connect through Telnet or rlogin.
Without a pseudo tty, no connection can take place.
7. Which layer of the 7 layer model provides services to the Application layer over the
Session layer connection?
Presentation.
8. What does the Mount protocol do ?
The Mount protocol returns a file handle and the name of the file system in which a
requested file resides. The message is sent to the client from the server after reception of a
client's request.
9. What is External Data Representation
External Data Representation is a method of encoding data within an RPC message, used to
ensure that the data is not system-dependent.
10. Which OSI Reference Layer controls application to application communication?
Session
11. BOOTP helps a diskless workstation boot. How does it get a message to the network
looking for its IP address and the location of its operating system boot files ?
BOOTP sends a UDP message with a subnetwork broadcast address and waits for a reply
from a server that gives it the IP address. The same message might contain the
name of the machine that has the boot files on it. If the boot image location is not specified,
the workstation sends another UDP message to query the server.
12. What is a DNS resource record
A resource record is an entry in a name server's database. There are several types of
resource records used, including name-to-address resolution information. Resource records
are maintained as ASCII files.
13. What protocol is used by DNS name servers
DNS uses UDP for communication between servers. It is a better choice than TCP because of
the improved speed a connectionless protocol offers. Of course, transmission reliability
suffers with UDP.
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
14. What is the difference between interior and exterior neighbor gateways
Interior gateways connect LANs of one organization, whereas exterior gateways connect the
organization to the outside world.
15. What is the HELLO protocol used for
The HELLO protocol uses time instead of distance to determine optimal routing. It is an
alternative to the Routing Information Protocol.
16. What are the advantages and disadvantages of the three types of routing tables
The three types of routing tables are fixed, dynamic, and fixed central. The fixed table must
be manually modified every
time there is a change. A dynamic table changes its information based on network traffic,
reducing the amount of manual maintenance. A fixed central table lets a manager
modify only one table, which is then read by other devices. The fixed central table reduces
the need to update each machine's table, as with the fixed table. Usually a
dynamic table causes the fewest problems for a network administrator, although the table's
contents can change without the administrator being aware of the change
.
17. What is a characteristic of Store and Forward switches?
They read the entire frame and check CRC before forwarding.
18. What is source route
It is a sequence of IP addresses identifying the route a datagram must follow. A source route
may optionally be included in an IP datagram header.
19. What is RIP (Routing Information Protocol)
It is a simple protocol used to exchange information between the routers.
20. What is SLIP (Serial Line Interface Protocol)
It is a very simple protocol used for transmission of IP datagrams across a serial line.
21. What is Proxy ARP
It is using a router to answer ARP requests. This will be done when the originating host
believes that a destination is local, when in fact is lies beyond router.
22. What is OSPF
It is an Internet routing protocol that scales well, can route traffic along multiple paths, and
uses knowledge of an Internet's topology to make accurate routing decisions.
23. What is Kerberos
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
It is an authentication service developed at the Massachusetts Institute of Technology.
Kerberos uses encryption to prevent intruders from discovering passwords and gaining
unauthorized access to files.
24. What is a Multi-homed Host
It is a host that has a multiple network interfaces and that requires multiple IP addresses is
called as a Multi-homed Host.
25. What is NVT (Network Virtual Terminal)
It is a set of rules defining a very simple virtual terminal interaction. The NVT is used in the
start of a Telnet session.
26. What is Gateway-to-Gateway protocol
It is a protocol formerly used to exchange routing information between Internet core routers.
27. What is BGP (Border Gateway Protocol)
It is a protocol used to advertise the set of networks that can be reached with in an
autonomous system. BGP enables this information to be shared with the autonomous
system. This is newer than EGP (Exterior Gateway Protocol).
28. What is autonomous system
It is a collection of routers under the control of a single administrative authority and that
uses a common Interior Gateway Protocol.
29. What is EGP (Exterior Gateway Protocol)
It is the protocol the routers in neighboring autonomous systems use to identify the set of
networks that can be reached within or via each autonomous system.
30. What is IGP (Interior Gateway Protocol)
It is any routing protocol used within an autonomous system.
31. What is Mail Gateway
It is a system that performs a protocol translation between different electronic mail delivery
protocols.
32. What is wide-mouth frog
Wide-mouth frog is the simplest known key distribution center (KDC) authentication
protocol.
33. What are Digrams and Trigrams
The most common two letter combinations are called as digrams. e.g. th, in, er, re and an.
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
The most common three letter combinations are called as trigrams. e.g. the, ing,
and, and ion.
34. What is silly window syndrome
It is a problem that can ruin TCP performance. This problem occurs when data are passed to
the sending TCP entity in large blocks, but an interactive application on the
receiving side reads 1 byte at a time.
35. What is region
When hierarchical routing is used, the routers are divided into what we call regions, with
each router knowing all the details about how to route packets to destinations
within its own region, but knowing nothing about the internal structure of other regions.
36. What is multicast routing
Sending a message to a group is called multicasting, and its routing algorithm is called
multicast routing.
37. What is traffic shaping
One of the main causes of congestion is that traffic is often busy. If hosts could be made to
transmit at a uniform rate,congestion would be less common. Another open loop
method to help manage congestion is forcing the packet to be transmitted at a more
predictable rate. This is called traffic shaping.
38. What is packet filter
Packet filter is a standard router equipped with some extra functionality. The extra
functionality allows every incoming or outgoing packet to be inspected. Packets meeting
some criterion are forwarded normally. Those that fail the test are dropped.
39. What is virtual path
Along any transmission path from a given source to a given destination, a group of virtual
circuits can be grouped together into what is called path.
40. What is virtual channel
Virtual channel is normally a connection from one source to one destination, although
multicast connections are also permitted. The other name for virtual channel is virtual circuit.
41. What is logical link control
One of two sublayers of the data link layer of OSI reference model, as defined by the IEEE
802 standard. This sublayer is responsible for maintaining the link between computers when
they are sending data across the physical network connection.
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
42. Why should you care about the OSI Reference Model
It provides a framework for discussing network operations and design.
43. What is the difference between routable and non- routable protocols
Routable protocols can work with a router and can be used to build large networks. NonRoutable
protocols are designed to work on small, local networks and cannot be used with a
router.
44. What is MAU
In token Ring , hub is called Multistation Access Unit(MAU).
45. Explain 5-4-3 rule
In a Ethernet network, between any two points on the network, there can be no more than
five network segments or four repeaters, and of those five segments only three of
segments can be populated.
46. What is the difference between TFTP and FTP application layer protocols
The Trivial File Transfer Protocol (TFTP) allows a local host to obtain files from a remote host
but does not provide reliability or security. It uses the fundamental packet delivery services
offered by UDP. The File Transfer Protocol (FTP) is the standard mechanism provided by TCP
/ IP for copying a file from one host to another. It uses the services offered by TCP and so is
reliable and secure. It establishes two connections (virtual circuits) between the hosts, one
for data transfer and another for control information.
47. What is the range of addresses in the classes of internet addresses
Class A 0.0.0.0 - 127.255.255.255
Class B 128.0.0.0 - 191.255.255.255
Class C 192.0.0.0 - 223.255.255.255
Class D 224.0.0.0 - 239.255.255.255
Class E 240.0.0.0 - 247.255.255.255
48. What is the minimum and maximum length of the header in the TCP segment and IP
datagram
The header should have a minimum length of 20 bytes and can have a maximum length of
60 bytes.
49. What is difference between ARP and RARP
The address resolution protocol (ARP) is used to associate the 32 bit IP address with the 48
bit physical address, used by a host or a router to find the physical address of
another host on its network by sending a ARP query packet that includes the IP address of
the receiver. The reverse address resolution protocol (RARP) allows a host to discover its
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
Internet address when it knows only its physical address.
50. What is ICMP
ICMP is Internet Control Message Protocol, a network layer protocol of the TCP/IP suite used
by hosts and gateways to send notification of datagram problems back to the sender. It uses
the echo test / reply to test whether a destination is reachable and responding. It also
handles both control and error messages.
51. What are the data units at different layers of the TCP / IP protocol suite
The data unit created at the application layer is called a message, at the transport layer the
data unit created is called either a segment or an user datagram, at the network layer the
data unit created is called the datagram, at the data link layer the datagram is encapsulated
in to a frame and finally transmitted as signals along the transmission media.
52. What is Project 802
It is a project started by IEEE to set standards that enable intercommunication between
equipment from a variety of
manufacturers. It is a way for specifying functions of the physical layer, the data link layer
and to some extent the network layer to allow for interconnectivity of major LAN
protocols.
It consists of the following:
802.1 is an internetworking standard for compatibility of different LANs and MANs across
protocols.
802.2 Logical link control (LLC) is the upper sublayer of the data link layer which is nonarchitecture-specific,
that is
remains the same for all IEEE-defined LANs.
Media access control (MAC) is the lower sublayer of the data link layer that contains some
distinct modules each
carrying proprietary information specific to the LAN product
being used. The modules are Ethernet LAN (802.3), Token ring LAN (802.4), Token bus LAN
(802.5).
802.6 is distributed queue dual bus (DQDB) designed to be used in MANs.
53. What is Bandwidth
Every line has an upper limit and a lower limit on the frequency of signals it can carry. This
limited range is called the
bandwidth.
54. Difference between bit rate and baud rate.
Bit rate is the number of bits transmitted during one second whereas baud rate refers to the
number of signal units per
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
second that are required to represent those bits.
baud rate = bit rate / N where N is no-of-bits represented by each signal shift.
55. What is MAC address
The address for a device as it is identified at the Media Access Control (MAC) layer in the
network architecture. MAC
address is usually stored in ROM on the network adapter card and is unique.
56. What is attenuation
The degeneration of a signal over distance on a network cable is called attenuation.
57. What is cladding
A layer of a glass surrounding the center fiber of glass inside a fiber-optic cable.
58. What is RAID
A method for providing fault tolerance by using multiple hard disk drives.
59. What is NETBIOS and NETBEUI
NETBIOS is a programming interface that allows I/O requests to be sent to and received
from a remote computer and it
hides the networking hardware from applications.
NETBEUI is NetBIOS extended user interface. A transport protocol designed by microsoft and
IBM for the use on small
subnets.
60. What is redirector
Redirector is software that intercepts file or prints I/O requests and translates them into
network requests. This comes under presentation layer.
61. What is Beaconing
The process that allows a network to self-repair networks problems. The stations on the
network notify the other stations on the ring when they are not receiving the transmissions.
Beaconing is used in Token ring and FDDI networks.
62. What is terminal emulation, in which layer it comes
Telnet is also called as terminal emulation. It belongs to application layer.
63. What is frame relay, in which layer it comes
Frame relay is a packet switching technology. It will operate in the data link layer.
64. What do you meant by "triple X" in Networks
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
The function of PAD (Packet Assembler Disassembler) is described in a document known as
X.3. The standard protocol has been defined between the terminal and the PAD, called X.28;
another standard protocol exists between hte PAD and the network, called X.29. Together,
these three recommendations are often called "triple X"
65. What is SAP
Series of interface points that allow other computers to communicate with the other layers
of network protocol stack.
66. What is subnet
A generic term for section of a large networks usually separated by a bridge or router.
67. What is Brouter
Hybrid devices that combine the features of both bridges and routers.
68. How Gateway is different from Routers
A gateway operates at the upper levels of the OSI model and translates information
between two completely different network architectures or data formats.
69. What are the different type of networking / internetworking devices
Repeater:
Also called a regenerator, it is an electronic device that operates only at physical layer. It
receives the signal in the
network before it becomes weak, regenerates the original bit pattern and puts the refreshed
copy back in to the link.
Bridges:
These operate both in the physical and data link layers of LANs of same type. They divide a
larger network in to smaller
segments. They contain logic that allow them to keep the traffic for each segment separate
and thus are repeaters that relay a frame only the side of the segment containing the
intended recipent and control congestion.
Routers:
They relay packets among multiple interconnected networks (i.e. LANs of different type).
They operate in the physical,
data link and network layers. They contain software that enable them to determine which of
the several possible paths is the best for a particular transmission.
Gateways:
They relay packets among networks that have different protocols (e.g. between a LAN and a
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
WAN). They accept a
packet formatted for one protocol and convert it to a packet formatted for another protocol
before forwarding it. They operate in all seven layers of the OSI model.
70. What is mesh network
A network in which there are multiple network links between computers to provide multiple
paths for data to travel.
71. What is passive topology
When the computers on the network simply listen and receive the signal, they are referred
to as passive because they don’t amplify the signal in any way. Example for passive topology
- linear bus.
72. What are the important topologies for networks
BUS topology:
In this each computer is directly connected to primary network cable in a single line.
Advantages:
Inexpensive, easy to install, simple to understand, easy to extend.
STAR topology:
In this all computers are connected using a central hub.
Advantages:
Can be inexpensive, easy to install and reconfigure and easy to trouble shoot physical
problems.
RING topology:
In this all computers are connected in loop.
Advantages:
All computers have equal access to network media, installation can be simple, and signal
does not degrade as much as
in other topologies because each computer regenerates it.
73. What are major types of networks and explain
Server-based network
Peer-to-peer network
Peer-to-peer network, computers can act as both servers sharing resources and as clients
using the resources.
Server-based networks provide centralized control of network resources and rely on server
computers to provide
security and network administration
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
74. What is Protocol Data Unit
The data unit in the LLC level is called the protocol data unit (PDU). The PDU contains of four
fields a destination
service access point (DSAP), a source service access point (SSAP), a control field and an
information field. DSAP, SSAP are addresses used by the LLC to identify the protocol stacks
on the receiving and sending machines that are generating and using the data. The control
field specifies whether the PDU frame is a information frame (I -
frame) or a supervisory frame (S - frame) or a unnumbered frame (U - frame).
75. What is difference between baseband and broadband transmission
In a baseband transmission, the entire bandwidth of the cable is consumed by a single signal.
In broadband transmission, signals are sent on multiple frequencies, allowing multiple
signals to be sent simultaneously.
76. What are the possible ways of data exchange
(i) Simplex (ii) Half-duplex (iii) Full-duplex.
77. What are the types of Transmission media
Signals are usually transmitted over some transmission media that are broadly classified in
to two categories.
Guided Media:
These are those that provide a conduit from one device to another that include twisted-pair,
coaxial cable and fiber-optic
cable. A signal traveling along any of these media is directed and is contained by the physical
limits of the medium. Twisted-pair and coaxial cable use metallic that accept and transport
signals in the form of electrical current. Optical fiber is a glass or plastic cable that accepts
and transports signals in the form of light.
Unguided Media:
This is the wireless media that transport electromagnetic waves without using a physical
conductor. Signals are
broadcast either through air. This is done through radio
communication, satellite communication and cellular telephony.
78. Difference between the communication and transmission.
Transmission is a physical movement of information and concern issues like bit polarity,
synchronization, clock etc.
Communication means the meaning full exchange of information between two
communication media.
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
79.The Internet Control Message Protocol occurs at what layer of the seven layer model?
Network
80.Which protocol resolves an IP address to a MAC address?
ARP
81.MIDI and MPEG are examples of what layer of the OSI seven layer model?
Presentation
82.What is the protocol number for UDP?
17
83.Which protocol is used for booting diskless workstations?
RARP
84.Which layer is responsible for putting 1s and 0s into a logical group?
Physical
85.What does 'P' mean when running a Trace?
Protocol unreachable
86.UDP works at which layer of the DOD model?
Host to Host
87.What is the default encapsulation of Netware 3.12?
802.2
88.Ping uses which Internet layer protocol?
ICMP
89.Which switching technology can reduce the size of a broadcast domain?
VLAN
90.What is the first step in data encapsulation?
User information is converted into data.
91.What is the protocol number for TCP?
6
92.What do you use the Aux port for?
做一个面试达人 美国编程师面试宝典,年薪十万美金不是梦
Modem
93.Repeaters work at which layer of the OSI model?
Physical
94.WAN stands for which of the following?
Wide Area Network
95.What ISDN protocol specifies concepts, terminology, and services?
I
96.LAN stands for which of the following?
Local Are Network
97.DHCP stands for
Dynamic Host Configuration Protocol
98.What does the acronym ARP stand for?
Address Resolution Protocol
99.Which layer is responsible for identifying and establishing the availability of the intended
communication partner?
Application.
100.Which OSI layer provides mechanical, electrical, procedural for activating, maintaining
physical link?
Physical
