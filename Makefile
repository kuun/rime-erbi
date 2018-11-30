build:
	./convert.py zzdperfect.txt rime-zzdperfect-data.txt
	cat zzdyx_perfect.dict.yaml.head rime-zzdperfect-data.txt > zzdyx_perfect.dict.yaml
	rm -f rime-zzdperfect-data.txt

release: build
	tar zcvf zzdyx_perfect.tar.gz zzdyx_perfect.dict.yaml zzdyx_perfect.schema.yaml
