class MyDictKeys:
    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        return (
            "dict_keys["
            + ", ".join(
                (
                    str(key)
                    for bucket in self.owner.buckets if bucket is not None
                    for key, value in bucket
                )
            )
            + "]"
        )

    def __len__(self):
      return len(self.owner)
