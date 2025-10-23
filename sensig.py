
def translate_signal(sig_type : str) -> int:
    signals = {
        "SIGKILL": 9,
        "SIGSEGV": 11,
        "SIGCONT": 18,
        "SIGSTOP": 19,
        "SIGTERM": 15
    }
    
    return signals[sig_type]
    
def init_action(pid : int, sig_type : str):

    from os import kill
    
    try:    
        sig_val = translate_signal(sig_type)
        kill(pid, sig_val)
        
    except KeyError:
        print(f"Unknown signal {sig_type}")

    except PermissionError:
        print(f"Operation not permitted {pid} <- {sig_type}")
    
    except ProcessLookupError:
        print(f"Process with process id {pid} not running")
        
 
def main():
    
    import platform
    
    if platform.system() != "Linux":
        print("This program is specifically made for linux-based OS")
        print("Aborting")
        
        exit(1)
    
    else:
        pid = int(input("Enter process id : "))
        sig_type = input("Enter signal : ")

        init_action(pid, sig_type)


if __name__ == "__main__":
    main()
    
    

