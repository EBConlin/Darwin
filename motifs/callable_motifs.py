class CallableMotif:
    """Abstract reusable motif component."""
    def __call__(self, *args):
        raise NotImplementedError("Call not implemented.")
