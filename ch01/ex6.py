import tensorflow as tf
a=tf.constant([[1,2],[3,4],[5,6]])
b=tf.constant([[10,11],[20,21],[30,31]])
c=tf.concat([a,b],0)
d=tf.concat([a,b],1)
e=tf.stack([a,b],0)
f=tf.stack([a,b],0)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)