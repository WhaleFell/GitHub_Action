# GitHub Action 定时运行仓库(测试用例)

## main.yml 配置文件

```yml
# name属性用来指定这个工作流的名字
name: HELLO GITHUB ACITON

# 这个部分用来指定能够触发工作流执行的事件
on:
  # 当对分支main进行push操作的时候，这个工作流就被触发了
  push:
    branches: [ main ]

# 工作流是由一个或多个的jobs构成的，在jobs里来说明要交给GitHub aciton执行的任务
jobs:
  # 这个jobs中的一个任务，名字叫build(随便怎么取)
  build:
    # 用来指定这个任务在什么操作系统上跑(服务器是GitHub免费提供的)
    runs-on: ubuntu-latest

    # 指出这个build任务的步骤
    steps:

      # 步骤，这里只写了一个步骤，目的是输出hello github acition
      - name: Run a one-line script
        run: echo Hello, github action!
```

## GitHub action 中的一些基本概念

1. `workflow` （工作流程）：持续集成一次运行的过程，就是一个 workflow。
2. `job` （任务）：一个 workflow 由一个或多个 jobs 构成，含义是一次持续集成的运行，可以完成多个任务。
3. `step`（步骤）：每个 job 由多个 step 构成，一步步完成。
4. `action` （动作）：每个 step 可以依次执行一个或多个命令（action）

## 完整配置

```yml
#字段1 name:用来指定workflow的名称，必备
name: Greeting from Mona
#字段2 on: 用来指定触发 workflow 的条件，通常是某些事件。
# 也可以是数组，如 on: [push, pull_request]
on: push
#字段3 jobs: workflow文件的主体是jobs字段，表示要执行的一项或多项任务
jobs:
#字段4: jobs.job_id: job_id是自定义的，比如这里写my_job
  my-job:
  # 字段5: jobs.job_id.name: 用来指定这个job的说明
    name: My Job
    # 字段6: jobs.job_id.runs-on: 用来指定这个job要在什么环境跑，也是必备的
    runs-on: ubuntu-latest
    # 字段7: jobs.job_id.steps: steps字段指定每个 Job 的运行步骤，可以包含一个或多个步骤。steps是一个数组，每个元素是一个step
    steps:
    # 字段8: name,具体的一个step的名字
    - name: Print a greeting
    # 字段9: env,具体的一个step会用到的环境变量
      env:
        MY_VAR: Hi there! My name is
        FIRST_NAME: Mona
        MIDDLE_NAME: The
        LAST_NAME: Octocat
        #字段10: run,具体的一个步骤运行的命令或者 action。
      run: |
        echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```
