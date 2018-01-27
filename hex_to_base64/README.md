# Convertion of Hexadecimal encoded string to Base64 Encoded String

When you have some binary data that you want to ship across a network, you generally don't do it by just streaming the bits and bytes over the wire in a raw format.

#### Why?
1. Because some media are made for streaming text. You never know -- some protocols may interpret your binary data as control characters
2. Your binary data could be screwed up because the underlying protocol might think that you've entered a special character combination
3. Can be easily corrupted and sniffed.

#### Why Hex? 
1. Readability. Hexadecimal uses digits that more closely resemble our usual base-10 counting system and it’s therefore easier to decide at a glance how big a number like e7 is as opposed to 11100111.
2. Higher information density. With 2 hexadecimal digits, we can express any number from 0 to 255. To do the same in binary, we need 8 digits. As we get bigger and bigger numbers, we start needing more and more digits and it becomes harder to deal with.

#### Why 64?
* Because you can generally rely on the same 64 characters being present in many character sets, and you can be reasonably confident that your data's going to end up on the other side of the wire uncorrupted.
