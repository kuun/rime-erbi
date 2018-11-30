all:
	./convert.py zzdperfect.txt rime-zzdperfect-data.txt
	cat zzdyx_perfect.dict.yaml.head rime-zzdperfect-data.txt > zzdyx_perfect.dict.yaml
	rm -f rime-zzdperfect-data.txt

