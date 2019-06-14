cd document/pve/

cd counters/
xelatex Counters.tex
pdf2htmlex --zoom 2 Counters.pdf
cd ..

cd gen4_evolution/
xelatex gen_4.tex
pdf2htmlex --zoom 2 gen_4.pdf
cd ..

cd guide/
xelatex Guide.tex
pdf2htmlex --zoom 2 Guide.pdf
cd ..

cd gym/
xelatex Gym.tex
pdf2htmlex --zoom 2 Gym.pdf
cd ..

cd legendary_raid/
xelatex Raid_bosses.tex
pdf2htmlex --zoom 2 Raid_bosses.pdf
cd ..

cd iv_determined_at_go/
xelatex iv_determined_at_go.tex
pdf2htmlex --zoom 2 iv_determined_at_go.pdf
cd ../..

cd ../pvp/counters
xelatex pvp.tex
pdf2htmlex --zoom 2 pvp.pdf
cd ../..
