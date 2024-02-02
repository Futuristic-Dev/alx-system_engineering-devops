# Learning Objectives

## General

1. **What is a PID?**
   - A PID (Process IDentifier) is a unique numerical identifier assigned to each running process in a computer system.

2. **What is a process?**
   - A process is an executing instance of a computer program. It has its own memory space, resources, and system data, allowing it to run independently.

3. **How to find a process’ PID?**
   - The `ps` command can be used to find the PID of a process. For example:
     ```bash
     ps aux | grep <process_name>
     ```

4. **How to kill a process?**
   - The `kill` command is used to terminate a process by sending a signal. For example:
     ```bash
     kill -9 <PID>
     ```

5. **What is a signal?**
   - A signal is a software interrupt delivered to a process, notifying it to perform a specific action, such as terminating or stopping.

6. **What are the 2 signals that cannot be ignored?**
   - The two signals that cannot be ignored are:
     - **SIGKILL (9):** Forces the process to immediately terminate.
     - **SIGSTOP (19 or 17):** Suspends the process until it receives a SIGCONT signal.


