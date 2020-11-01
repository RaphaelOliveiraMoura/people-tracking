tiledlayout(2,2,'TileSpacing','none')

create_chart('Frios', 1, [6 1 1])
create_chart('Bebidas', 2, [4.5 1 1])
create_chart('Limpeza', 3, [5.3 1.1 1])
create_chart('Hortifruti', 4, [5.5 1 1])

function f_create_chart = create_chart(chart_name, device_id, position)
    readAPIKey = 'V79KCD77H54DO184';
    readChannelID = 1213641;
    
    fieldID1 = 1;
    fieldID2 = 2;
    fieldID3 = 3;
    fieldID4 = 4;
    
    ammount_data = 50;
    
    array_id = thingSpeakRead(readChannelID, 'Field', fieldID1, 'NumPoints', ammount_data, 'ReadKey', readAPIKey);
    array_x = thingSpeakRead(readChannelID, 'Field', fieldID2, 'NumPoints', ammount_data, 'ReadKey', readAPIKey);
    array_y = thingSpeakRead(readChannelID, 'Field', fieldID3, 'NumPoints', ammount_data, 'ReadKey', readAPIKey);
    table_date = thingSpeakRead(readChannelID, 'OutputFormat','table', 'Field', fieldID4, 'NumPoints', ammount_data, 'ReadKey', readAPIKey);
    
    array_date = table2array(table_date(:,2));
    
    new_x_array = {};
    new_y_array = {};
    new_z_array = {};
    new_color_array = {};
    
    for index = 1:length(array_x)
        index_item_x = array_x(index);
        index_item_y = array_y(index);
        [hours, minutes, seconds] = hms(datetime(array_date(index), 'InputFormat', 'yyyy-MM-dd HH:mm:ss.SSS'));
        
        is_morning = hours >= 6 && hours < 12;
        is_afternoon = hours >= 12 && hours <= 18;
        is_nigth = hours > 18 || hours < 6;
    
        if array_id(index) ~= device_id
            continue;
        end
        
        if index == 1    
            new_x_array{1} = index_item_x;
            new_y_array{1} = index_item_y;
            new_z_array{1} = 1;
            if is_morning
                new_color_array{1,1} = 0;
                new_color_array{1,2} = 1;
                new_color_array{1,3} = 0;
            elseif is_afternoon
                new_color_array{1,1} = 1;
                new_color_array{1,2} = 0;
                new_color_array{1,3} = 0;
            elseif is_nigth
                new_color_array{1,1} = 0;
                new_color_array{1,2} = 0;
                new_color_array{1,3} = 1;
            end
        else        
            
            already_exists_index = -1;
            
            for index2 = 1:length(new_x_array)
               index2_item_x = new_x_array(index2);
               index2_item_y = new_y_array(index2);
               
               if index2 == 1
                    continue;
               end
               
               if((index_item_x == cell2mat(index2_item_x)) && (index_item_y == cell2mat(index2_item_y)) )
                   
                   if length(new_color_array) == 0
                       
                       index2_color_red = new_color_array{index2, 1};
                       index2_color_green = new_color_array{index2, 2};
                       index2_color_blue = new_color_array{index2, 3};
                       
                       new_color_array{index2}
                       index2_color_red
                       index2_color_green 
                       index2_color_blue 
                       
                       at_same_period = (index2_color_red == 1 && is_afternoon) || (index2_color_green == 1 && is_morning) || (index2_color_blue == 1 && is_nigth)
                       
                       if ~at_same_period
                            already_exists_index = index2;
                       end
                   else
                       already_exists_index = index2;
                   end
               end
            end
            
            if already_exists_index == -1
                new_x_array{length(new_x_array) + 1} = index_item_x;
                new_y_array{length(new_y_array) + 1} = index_item_y;
                new_z_array{length(new_z_array) + 1} = 1;
                if is_morning
                    new_color_array{length(new_color_array) + 1, 1} = 0;
                    new_color_array{length(new_color_array) + 1, 2} = 1;
                    new_color_array{length(new_color_array) + 1, 3} = 0;
                elseif is_afternoon
                    new_color_array{length(new_color_array) + 1, 1} = 1;
                    new_color_array{length(new_color_array) + 1, 2} = 0;
                    new_color_array{length(new_color_array) + 1, 3} = 0;
                elseif is_nigth
                    new_color_array{length(new_color_array) + 1, 1} = 0;
                    new_color_array{length(new_color_array) + 1, 2} = 0;
                    new_color_array{length(new_color_array) + 1, 3} = 1;
                end
            else
                new_z_array{already_exists_index } = new_z_array{index2} + 1;
            end 
        end
    end
    
    chart_colors = 'red';
    
    if length(new_color_array) > 0
        chart_colors = cell2mat(new_color_array);
    end
   
    chart = nexttile;
    bubblechart(chart, cell2mat(new_x_array), cell2mat(new_y_array), cell2mat(new_z_array), chart_colors );
    bubblesize(chart, [10 15]);
    
    set(gca,'XTick',[], 'YTick', []);
   
    lgd = legend({'a', 'b'}, 'Location', 'southwest');

end

