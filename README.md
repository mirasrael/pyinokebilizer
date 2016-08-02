# Python INVOKE staBILIZER

This library provides compatible interface subset between multiple `invoke` versions.
I.e. you can use invoke 0.13 interface while you have only invoke 0.10 installed in your system.
It also provides additional helpful methods, like `run_all`, which may be used for running multiple tasks (with individula failure handling) inside of single task.

## Usage

```python
from invokebilizer.v0_13 import task, run_all

@task
def say_hello(ctx):
    ctx.run("echo 'Hello world'")


@task
def say_goodbye(ctx):
    ctx.run("echo Goodbye")


@task
def say_hello_and_say_goodbye(ctx):
    run_all(ctx, say_hello, say_goodbye)
```

For more examples you can view `test` folder.
