import logging

def run(test, params, env):

    """
    Uptime test for virt guests:

    1) Boot up a VM.
    2) Establish a remote connection to it.
    3) Run the 'uptime' command and log its results.

    :param test: QEMU test object.
    :param params: Dictionary with the test parameters.
    :param env: Dictionary with test environment.
    """

    vm = env.get_vm(params["main_vm"])
    details = vm.make_create_command()
    for key, detail in details:
        logging.info("{} {}".format(key, detail))
    vm.verify_alive()
    timeout = float(params.get("login_timeout", 240))
    session = vm.wait_for_login(timeout=timeout)
    uptime = session.cmd("uptime")
    logging.info("Guest uptime result is: %s", uptime)
    session.close()