# print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
# 将 objects 打印到 file 指定的文本流，以 sep 分隔并在末尾加上 end。 sep, end, file 和 flush 如果存在，它们必须以关键字参数的形式给出。

# 将 objects 打印到 file 指定的文本流，以 sep 分隔并在末尾加上 end。
print('test')
print('test1', 'test2', 'test3')
# sep, end, file 和 flush 如果存在，它们必须以关键字参数的形式给出。
print('test', end='test_end')
print('test1', 'test2', 'test3', sep='_')
#
# 所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end。 sep 和 end 都必须为字符串；它们也可以为 None，这意味着使用默认值。 如果没有给出 objects，则 print() 将只写入 end。

# 所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end。
print(1, 1.23, None, True, [1, 2], sep='_', end='*')
# sep 和 end 都必须为字符串；
print(1, 1.23, None, True, [1, 2], sep=1, end='*')
# 它们也可以为 None，这意味着使用默认值。
print('test1', 'test2', 'test3', sep=None, end=None)
# 如果没有给出 objects，则 print() 将只写入 end。
print()
print(end='test_end')

#
# file 参数必须是一个具有 write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout。 由于要打印的参数会被转换为文本字符串，因此 print() 不能用于二进制模式的文件对象。 对于这些对象，应改用 file.write(...)。

# file 参数必须是一个具有 write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout。
# print('test', file=None)
f = open('test.txt', 'w')
print('test', file=f)
f.close()
#
# 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为真值，流会被强制刷新。
#
# 在 3.3 版更改: 增加了 flush 关键字参数。

# 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为真值，流会被强制刷新。
import time
for test in ["test1", "test2", "test3"]:
    print(test, end='')
    time.sleep(2)
for test in ["test1", "test2", "test3"]:
    print(test, end='', flush=True)
    time.sleep(2)

f = open('test_file2.txt', 'w')
print('test1', file=f)
time.sleep(10)
f.close()

f = open('test_file3.txt', 'w')
print('test1', file=f, flush=True)
time.sleep(10)
f.close()





