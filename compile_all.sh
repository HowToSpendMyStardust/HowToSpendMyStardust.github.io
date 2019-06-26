cd document/pve/

cd counters/
xelatex Counters.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 Counters.pdf
cd ..

cd guide/
xelatex Guide.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 Guide.pdf
cd ..

cd gym/
xelatex Gym.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 Gym.pdf
cd ..

cd legendary_raid/
xelatex Raid_bosses.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 Raid_bosses.pdf
cd ..

cd iv_determined_at_go/
xelatex iv_determined_at_go.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 iv_determined_at_go.pdf
cd ..

cd fr/guide_fr
xelatex Guide.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 Guide.pdf
cd ..

cd iv_determined_at_go_fr/
xelatex iv_determined_at_go.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 iv_determined_at_go.pdf
cd ../../..

cd pvp/counters
xelatex pvp.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 pvp.pdf
cd ../..

cd infographics/

cd bag/
xelatex bag.tex
pdf2htmlex --zoom 1.6 --hdpi 432 --vdpi 432 bag.pdf
cd ..

cd daily_task/
xelatex daily_task.tex
pdf2htmlex --zoom 1.6 --hdpi 432 --vdpi 432 daily_task.pdf
cd ..

cd lucky_trade/
xelatex Lucky_trade.tex
pdf2htmlex --zoom 1.6 --hdpi 432 --vdpi 432 Lucky_trade.pdf
cd ..

cd power_up_cost/
xelatex power_up.tex
pdf2htmlex --zoom 1.6 --hdpi 432 --vdpi 432 power_up.pdf
cd ..

cd trading_cost/
xelatex trading_cost.tex
pdf2htmlex --zoom 1.6 --hdpi 432 --vdpi 432 trading_cost.pdf
cd ..

cd gen4_evolution/
xelatex gen_4.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 gen_4.pdf
cd ..

cd second_charged_moves/
xelatex second_charged_moves.tex
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 second_charged_moves.pdf
cd ..

cd name/
pdf2htmlex --zoom 1.1 --hdpi 432 --vdpi 432 name.pdf
cd ..


cd ..

cd calendar/
pdf2htmlex --zoom 1 --hdpi 432 --vdpi 432 calendar_summer2019.pdf
cd ..
