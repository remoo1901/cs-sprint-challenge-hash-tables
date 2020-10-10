# Your code here
import ntpath


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for path in files:
        fileName  = ntpath.basename(path)
        if fileName in cache:
            cache[fileName].append(path)
        else:
            cache[fileName] = [path]

    for fileName in queries:
        if fileName in cache:
            result.extend(cache[fileName])            


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
