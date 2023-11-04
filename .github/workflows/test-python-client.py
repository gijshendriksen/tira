name: Test Python Client
on: [push]

jobs:
  image:

    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      -
        name: Checkout
        uses: actions/checkout@v3
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v2
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Build Image
        run: |
          cd python-client
          echo running on branch ${GITHUB_REF##*/}
          make run-tests

