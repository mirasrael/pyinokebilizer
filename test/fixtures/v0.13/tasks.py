from invokebilizer.v0_13 import task, run_all


@task
def say_hello(ctx):
    ctx.run("echo 'Hello world'")


@task
def say_goodbye(ctx):
    ctx.run("echo Goodbye")


@task(say_hello)
def greeting(ctx):
    ctx.run('echo Greeting!')


@task
def say_hello_and_say_goodbye(ctx):
    run_all(ctx, say_hello, say_goodbye)
