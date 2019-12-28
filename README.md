# Spacing

**Spacing** is a web application built using Django, SQLite, RESTFUL Routes with a few more frameworks and middle-wares used as the application is developed. This application is used to help people memorize anything they want to build as long-term memory. Which is according to the [learning curve](https://en.wikipedia.org/wiki/Learning_curve) that was identified by [Hermann Ebbinghaus](https://en.wikipedia.org/wiki/Hermann_Ebbinghaus).

## Description

### Forgetting curve
The [forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve) hypothesizes the decline of memory retention in time. This curve shows how information is lost over time when there is no attempt to retain it.[1] A related concept is the strength of memory that refers to the durability that memory traces in the brain. The stronger the memory, the longer period of time that a person is able to recall it. A typical graph of the forgetting curve purports to show that humans tend to halve their memory of newly learned knowledge in a matter of days or weeks unless they consciously review the learned material.

![alt text](https://upload.wikimedia.org/wikipedia/commons/4/4e/ForgettingCurve.svg)

### Forgetting curve
The [spacing effect](https://en.wikipedia.org/wiki/Spacing_effect) demonstrates that learning is more effective when study sessions are spaced out. This effect shows that more information is encoded into long-term memory by spaced study sessions, that is known as spaced presentation, than by "cramming", or massed studying or massed presentation, such as in studying for an exam only the night before.

| Spaced Time |  Memory |
| ----------- | ------- |
|   1st day   |  58.2%  |
|   2nd day   |  44.6%  |
|   4th day   |  38.5%  |
|   7th day   |  25.3%  |
|   15th day  |  20.2%  |

According to the forgetting curve, this web application will show the information user input in 1, 2, 4, 7, 15 days.

### RESTFUL Routes

Application of REpresentational State Transfer (REST)

| Name    | Path                    | HTTP Verb | Purpose                                                 |
| ------- | ----------------------- | --------- | ------------------------------------------------------- |
| Index   | `/spacing`              | GET       | List all information                                    |
| Create  | `/spacing/create`       | POST      | Create new information to memorize                      |
| Register| `/spacing/register`     | POST      | Create a new account                                    |
| Login   | `/login`                | GET       | Make user to login                                      |
| List    | `/spacing/list`         | GET       | Show info about one specific user                       |
| Delete  | `/spacing/list/<int:id>`| POST      | Delete the info about one specific user                 |
