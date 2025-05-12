from darwin_loop import DarwinLoop

def main():
    loop = DarwinLoop(config_path="config.yaml")
    loop.run()

if __name__ == "__main__":
    main()